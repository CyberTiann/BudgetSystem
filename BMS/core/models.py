from django.db import models
from decimal import Decimal

# Create your models here.
class workgroup(models.Model):
    name = models.CharField(max_length=255, unique=True, default='Default Workgroup')

    class Meta:
        verbose_name = 'Workgroup'

    def __str__(self):
        return self.name
    
class reference(models.Model):
    reference = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Reference'
    def __str__(self):
        return str(self.reference)
    
class account_code(models.Model):
    code = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Account Code'
    def __str__(self):
        return str(self.code)
    
class account_name(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Account Name'

    def __str__(self):
        return str(self.name)
    
class payee(models.Model):
    payee = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Payee'

    def __str__(self):
        return str(self.payee)
    
class budget_category(models.Model):
    category = models.CharField(max_length=255, null=True, blank=True)
    workgroup = models.ForeignKey(workgroup, on_delete=models.SET_NULL, related_name='budget_categories', null=True)
    annual_budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'), editable=False)
    unutilized = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'), editable=False)
    percentage = models.FloatField(default=0.0, editable=False)

    class Meta:
        verbose_name = 'Budget Category'

    def save(self, *args, **kwargs):
        self.unutilized = self.annual_budget - self.total_amount if self.annual_budget is not None else None
        self.percentage = (self.unutilized / self.annual_budget * 100) if self.annual_budget > 0 else 0
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.category} ({self.workgroup.name})"

class sources_classification(models.Model):
    classification = models.CharField(max_length=255, null=True, blank=True) 

    class Meta:
        verbose_name = 'Sources Classification'

    def __str__(self):
        return str(self.classification)
class sl_code_and_name(models.Model):
    sl_code = models.CharField(max_length=255, null=True, blank=True)    
    def __str__(self):
        return str(self.sl_code)
#add use of funds dropdown
class choose(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)     #source or use

    

class budget(models.Model):

    date = models.DateField()
    account_code = models.ForeignKey(account_code, on_delete=models.SET_NULL, null=True,blank=True, related_name="ac_budget")
    account_name = models.ForeignKey(account_name, on_delete=models.SET_NULL, null=True, blank=True, related_name="an_budget")
    workgroup = models.ForeignKey(workgroup, on_delete=models.SET_NULL, null=True, blank=True, related_name="budgets")
    payee = models.ForeignKey(payee,on_delete=models.SET_NULL, null=True, blank=True)
    reference = models.ForeignKey(reference, on_delete=models.SET_NULL, null=True, blank=True, related_name="rf_budget")
    reference_number = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True,blank=True)
    budget_category = models.ForeignKey(budget_category, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.CharField(max_length=255, null=True, blank=True)
    unutilized = models.DecimalField(max_digits=10, decimal_places=2, editable=False, null=True, blank=True)
    percentage = models.FloatField(editable=False, null=True, blank=True)

    class Meta:
        verbose_name = 'PS Data Entry and Monitoring'
    def __str__(self):
        return f"{self.workgroup} - {self.amount}"

    def save(self, *args, **kwargs):
        if self.amount is not None:
            amount_decimal = Decimal(self.amount) if self.amount else Decimal(0)
            if self.budget_category:
                self.budget_category.total_amount += amount_decimal
                self.budget_category.save()

            if self.budget_category and self.budget_category.annual_budget is not None:
                self.unutilized = self.budget_category.annual_budget - amount_decimal
                self.percentage = (amount_decimal / self.budget_category.annual_budget * 100) if self.budget_category.annual_budget > 0 else 0
            else:
                self.unutilized = None
                self.percentage = None

        super().save(*args, **kwargs)

class funds(models.Model):
    date = models.DateField()
    account_code = models.ForeignKey(account_code, on_delete=models.SET_NULL, null=True,blank=True, related_name="ac_funds")
    account_name = models.ForeignKey(account_name, on_delete=models.SET_NULL, null=True, blank=True, related_name="an_funds")
    workgroup = models.ForeignKey(workgroup, on_delete=models.SET_NULL, null=True, blank=True, related_name="funds")
    sl_code = models.ForeignKey(sl_code_and_name, on_delete=models.SET_NULL, null=True, blank=True, related_name="wg_funds")
    received_from = models.CharField(max_length=255, null=True, blank=True)
    reference = models.ForeignKey(reference, on_delete=models.SET_NULL, null=True, blank=True, related_name="rf_funds")
    reference_number = models.CharField(max_length=255, null=True, blank=True)
    sources_classification = models.ForeignKey(sources_classification, on_delete=models.SET_NULL, null=True,blank=True)
    amount = models.CharField(max_length=255, null=True, blank=True)
    unutilized = models.DecimalField(max_digits=10, decimal_places=2, editable=False, null=True, blank=True)
    percentage = models.FloatField(editable=False, null=True, blank=True)
    budget_category = models.ForeignKey(budget_category, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Sources of Funds Data Entry and Monitoring'
    def __str__(self):
        return f"{self.workgroup} - {self.amount}"
    
    def save(self, *args, **kwargs):
        if self.amount is not None:
            amount_decimal = Decimal(self.amount) if self.amount else Decimal(0)
            if self.budget_category:
                self.budget_category.total_amount += amount_decimal
                self.budget_category.save()

            if self.budget_category and self.budget_category.annual_budget is not None:
                self.unutilized = self.budget_category.annual_budget - amount_decimal
                self.percentage = (amount_decimal / self.budget_category.annual_budget * 100) if self.budget_category.annual_budget > 0 else 0
            else:
                self.unutilized = None
                self.percentage = None

        super().save(*args, **kwargs)

class mooe(models.Model):
    

    date = models.DateField()
    account_code = models.ForeignKey(account_code, on_delete=models.SET_NULL, null=True,blank=True, related_name="ac_mooe")
    account_name = models.ForeignKey(account_name, on_delete=models.SET_NULL, null=True, blank=True, related_name="an_mooe")
    workgroup = models.ForeignKey(workgroup, on_delete=models.SET_NULL, null=True, blank=True, related_name="mooes")
    payee = models.ForeignKey(payee,on_delete=models.SET_NULL, null=True, blank=True)
    reference = models.ForeignKey(reference, on_delete=models.SET_NULL, null=True, blank=True, related_name="rf_mooe")
    reference_number = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True,blank=True)
    budget_category = models.ForeignKey(budget_category, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.CharField(max_length=255, null=True, blank=True)
    unutilized = models.DecimalField(max_digits=10, decimal_places=2, editable=False, null=True, blank=True)
    percentage = models.FloatField(editable=False, null=True, blank=True)

    class Meta:
        verbose_name = 'MOOE Data Entry and Monitoring'
    def __str__(self):
        return f"{self.workgroup} - {self.amount}"

    def save(self, *args, **kwargs):
        if self.amount is not None:
            amount_decimal = Decimal(self.amount) if self.amount else Decimal(0)
            if self.budget_category:
                self.budget_category.total_amount += amount_decimal
                self.budget_category.save()

            if self.budget_category and self.budget_category.annual_budget is not None:
                self.unutilized = self.budget_category.annual_budget - amount_decimal
                self.percentage = (amount_decimal / self.budget_category.annual_budget * 100) if self.budget_category.annual_budget > 0 else 0
            else:
                self.unutilized = None
                self.percentage = None

        super().save(*args, **kwargs)