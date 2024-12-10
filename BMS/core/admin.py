import pandas as pd
from django.http import HttpResponse
from django.contrib import admin
from .models import sl_code_and_name, mooe, budget, funds, workgroup, reference, account_name, account_code, payee, budget_category, sources_classification
from django.db.models import Q

# Function to export queryset to Excel
def export_to_excel(modeladmin, request, queryset):
    # Create a list to hold the data
    data = []
    
    # Check if the model is budget_category and handle accordingly
    if modeladmin.model == budget_category:
        for obj in queryset:
            data.append({
                'category': obj.category,
                'workgroup': obj.workgroup.name if obj.workgroup else None,
                'annual_budget': obj.annual_budget,
                'total_amount': obj.total_amount,
                'unutilized': obj.unutilized,
                'percentage': obj.percentage,
            })
    else:
        # Iterate through the queryset and fetch related values for other models
        for obj in queryset:
            data.append({
                'date': obj.date,
                'workgroup': obj.workgroup.name if obj.workgroup else None,
                'account_code': obj.account_code.code if obj.account_code else None,
                'account_name': obj.account_name.name if obj.account_name else None,
                'payee': obj.payee.payee if obj.payee else None,
                'reference': obj.reference,
                'reference_number': obj.reference_number,
                'budget_category': obj.budget_category.category if obj.budget_category else None,
                'amount': obj.amount,
            })
    
    # Create a Pandas DataFrame from the data list
    df = pd.DataFrame(data)
    
    # Change column names: capitalize, remove underscores, and replace with spaces
    df.columns = [col.replace('_', ' ').capitalize() for col in df.columns]
    
    # Calculate totals for annual_budget, total_amount, and unutilized if applicable
    if modeladmin.model == budget_category:
        total_annual_budget = df['Annual budget'].sum()
        total_amount = df['Total amount'].sum()
        total_unutilized = df['Unutilized'].sum()
        
        # Append the totals as a new row
        totals_row = pd.DataFrame({
            'Category': ['Total'],
            'Workgroup': [''],
            'Annual budget': [total_annual_budget],
            'Total amount': [total_amount],
            'Unutilized': [total_unutilized],
            'Percentage': ['']
        })
        df = pd.concat([df, totals_row], ignore_index=True)
    
    # Create an HTTP response with the Excel file
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="export.xlsx"'
    df.to_excel(response, index=False)
    return response

# Function to duplicate selected objects
def duplicate_budget(modeladmin, request, queryset):
    for obj in queryset:
        obj.pk = None  # Set primary key to None to create a new instance
        obj.amount = None  # Exclude amount
        obj.budget_category = None  # Exclude budget category
        obj.unutilized = None  # Exclude unutilized
        obj.percentage = None  # Exclude percentage
        obj.save()  # Save the new instance

def duplicate_funds(modeladmin, request, queryset):
    for obj in queryset:
        obj.pk = None  # Set primary key to None to create a new instance
        obj.amount = None  # Exclude amount
        obj.unutilized = None  # Exclude unutilized
        obj.percentage = None  # Exclude percentage
        obj.save()  # Save the new instance

def duplicate_mooe(modeladmin, request, queryset):
    for obj in queryset:
        obj.pk = None  # Set primary key to None to create a new instance
        obj.amount = None  # Exclude amount
        obj.budget_category = None  # Exclude budget category
        obj.unutilized = None  # Exclude unutilized
        obj.percentage = None  # Exclude percentage
        obj.save()  # Save the new instance

# Register your models here.
@admin.register(budget_category)
class BudgetCategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'workgroup', 'annual_budget', 'total_amount', 
                    'unutilized', 'format_percentage')  # Use the custom method for percentage
    search_fields = ('category',)  # Allow searching by category name
    list_filter = ('category', 'workgroup')  # Added workgroup filter to separate by workgroup

    actions = [export_to_excel]  # Add the export action

    def format_percentage(self, obj):
        return f"{obj.percentage}%" if obj.percentage is not None else ""
    format_percentage.short_description = 'Percentage'  # Set column name in admin

@admin.register(budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('date', 'workgroup', 'account_code', 'account_name', 'payee', 
                   'reference', 'reference_number', 'budget_category', 'amount', 
                   'unutilized', 'format_percentage')
    list_filter = ('date', 'workgroup', 'budget_category')
    search_fields = ('reference_number', 'description', 'date__year')  # Allow searching by year
    date_hierarchy = 'date'
    actions = [export_to_excel, duplicate_budget]  # Add the duplicate action

    def format_percentage(self, obj):
        return f"{obj.percentage}%" if obj.percentage is not None else ""
    format_percentage.short_description = 'Percentage'  # Set column name in admin

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        if search_term.isdigit():  # Check if the search term is a number (year)
            queryset |= self.model.objects.filter(date__year=search_term)  # Filter by year
        return queryset, use_distinct

@admin.register(funds)
class FundsAdmin(admin.ModelAdmin):
    list_display = ('date', 'workgroup', 'account_code', 'account_name', 
                   'sl_code', 'received_from', 'reference', 'reference_number', 
                   'sources_classification', 'amount', 
                   'unutilized', 'format_percentage')
    list_filter = ('date', 'workgroup', 'sources_classification')
    search_fields = ('reference_number', 'received_from', 'sl_code', 'date__year')  # Allow searching by year
    date_hierarchy = 'date'
    actions = [export_to_excel, duplicate_funds]  # Add the duplicate action

    def format_percentage(self, obj):
        return f"{obj.percentage}%" if obj.percentage is not None else ""
    format_percentage.short_description = 'Percentage'  # Set column name in admin

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        if search_term.isdigit():  # Check if the search term is a number (year)
            queryset |= self.model.objects.filter(date__year=search_term)  # Filter by year
        return queryset, use_distinct

@admin.register(mooe)
class MOOEAdmin(admin.ModelAdmin):
    list_display = ('date', 'workgroup', 'account_code', 'account_name', 'payee', 
                   'reference', 'reference_number', 'budget_category', 'amount', 
                   'unutilized', 'format_percentage')
    list_filter = ('date', 'workgroup', 'budget_category')
    search_fields = ('reference_number', 'description', 'date__year')  # Allow searching by year
    date_hierarchy = 'date'
    actions = [export_to_excel, duplicate_mooe]  # Add the duplicate action

    def format_percentage(self, obj):
        return f"{obj.percentage}%" if obj.percentage is not None else ""
    format_percentage.short_description = 'Percentage'  # Set column name in admin

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        if search_term.isdigit():  # Check if the search term is a number (year)
            queryset |= self.model.objects.filter(date__year=search_term)  # Filter by year
        return queryset, use_distinct

admin.site.register(workgroup)
admin.site.register(reference)
admin.site.register(account_name)
admin.site.register(account_code)
admin.site.register(payee)
admin.site.register(sources_classification)
admin.site.register(sl_code_and_name)
