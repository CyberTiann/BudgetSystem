import pandas as pd
from django.http import HttpResponse
from django.contrib import admin
from .models import sl_code_and_name, mooe, budget, funds, workgroup, reference, account_name, account_code, payee, budget_category, sources_classification

# Function to export queryset to Excel
def export_to_excel(modeladmin, request, queryset):
    # Create a list to hold the data
    data = []
    
    # Iterate through the queryset and fetch related values
    for obj in queryset:
        data.append({
            'date': obj.date,
            'workgroup': obj.workgroup.workgroup if obj.workgroup else None,  # Assuming workgroup has a 'name' field
            'account_code': obj.account_code.code if obj.account_code else None,  # Assuming account_code has a 'code' field
            'account_name': obj.account_name.name if obj.account_name else None,  # Assuming account_name has a 'name' field
            'payee': obj.payee.payee if obj.payee else None,  # Assuming payee has a 'name' field
            'reference': obj.reference,
            'reference_number': obj.reference_number,
            'budget_category': obj.budget_category.category if obj.budget_category else None,  # Assuming budget_category has a 'name' field
            'amount': obj.amount,
        })
    
    # Create a Pandas DataFrame from the data list
    df = pd.DataFrame(data)
    
    # Change column names: capitalize, remove underscores, and replace with spaces
    df.columns = [col.replace('_', ' ').capitalize() for col in df.columns]
    
    # Create an HTTP response with the Excel file
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="export.xlsx"'
    df.to_excel(response, index=False)
    return response

# Register your models here.
@admin.register(budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('date', 'workgroup', 'account_code', 'account_name', 'payee', 
                   'reference', 'reference_number', 'budget_category', 'amount')
    list_filter = ('date', 'workgroup', 'budget_category')
    search_fields = ('reference_number', 'description')
    date_hierarchy = 'date'
    actions = [export_to_excel]  # Add the export action

@admin.register(funds)
class FundsAdmin(admin.ModelAdmin):
    list_display = ('date', 'workgroup', 'account_code', 'account_name', 
                   'sl_code', 'received_from', 'reference', 'reference_number', 
                   'sources_classification', 'amount')
    list_filter = ('date', 'workgroup', 'sources_classification')
    search_fields = ('reference_number', 'received_from', 'sl_code')
    date_hierarchy = 'date'
    actions = [export_to_excel]  # Add the export action

@admin.register(mooe)
class MOOEAdmin(admin.ModelAdmin):  # Fixed class name to avoid duplication
    list_display = ('date', 'workgroup', 'account_code', 'account_name', 'payee', 
                   'reference', 'reference_number', 'budget_category', 'amount')
    list_filter = ('date', 'workgroup', 'budget_category')
    search_fields = ('reference_number', 'description')
    date_hierarchy = 'date'
    actions = [export_to_excel]  # Add the export action

admin.site.register(workgroup)
admin.site.register(reference)
admin.site.register(account_name)
admin.site.register(account_code)
admin.site.register(payee)
admin.site.register(budget_category)
admin.site.register(sources_classification)
admin.site.register(sl_code_and_name)
