from django.db import models

# Create your models here.
class workgroup(models.Model):
    workgroup = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return str(self.workgroup)
class reference(models.Model):
    reference = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return str(self.reference)
class account_code(models.Model):
    code = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return str(self.code)
class account_name(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return str(self.name)
class payee(models.Model):
    payee = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return str(self.payee)
class budget_category(models.Model):
    category = models.CharField(max_length=255, null=True, blank=True)    
    def __str__(self):
        return str(self.category)
class sources_classification(models.Model):
    classification = models.CharField(max_length=255, null=True, blank=True)    
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
    workgroup = models.ForeignKey(workgroup, on_delete=models.SET_NULL, null=True, blank=True, related_name="wg_budget")
    payee = models.ForeignKey(payee,on_delete=models.SET_NULL, null=True, blank=True)
    reference = models.ForeignKey(reference, on_delete=models.SET_NULL, null=True, blank=True, related_name="rf_budget")
    reference_number = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True,blank=True)
    budget_category = models.ForeignKey(budget_category, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'PS Data Entry and Monitoring'
    def __str__(self):
        return f"{self.workgroup} - {self.amount}"

class funds(models.Model):
    date = models.DateField()
    account_code = models.ForeignKey(account_code, on_delete=models.SET_NULL, null=True,blank=True, related_name="ac_funds")
    account_name = models.ForeignKey(account_name, on_delete=models.SET_NULL, null=True, blank=True, related_name="an_funds")
    workgroup = models.ForeignKey(workgroup, on_delete=models.SET_NULL, null=True, blank=True, related_name="wg_funds")
    sl_code = models.ForeignKey(sl_code_and_name, on_delete=models.SET_NULL, null=True, blank=True, related_name="wg_funds")
    received_from = models.CharField(max_length=255, null=True, blank=True)
    reference = models.ForeignKey(reference, on_delete=models.SET_NULL, null=True, blank=True, related_name="rf_funds")
    reference_number = models.CharField(max_length=255, null=True, blank=True)
    sources_classification = models.ForeignKey(sources_classification, on_delete=models.SET_NULL, null=True,blank=True)
    amount = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Sources of Funds Data Entry and Monitoring'
    def __str__(self):
        return f"{self.workgroup} - {self.amount}"
    
class mooe(models.Model):
    

    date = models.DateField()
    account_code = models.ForeignKey(account_code, on_delete=models.SET_NULL, null=True,blank=True, related_name="ac_mooe")
    account_name = models.ForeignKey(account_name, on_delete=models.SET_NULL, null=True, blank=True, related_name="an_mooe")
    workgroup = models.ForeignKey(workgroup, on_delete=models.SET_NULL, null=True, blank=True, related_name="wg_mooe")
    payee = models.ForeignKey(payee,on_delete=models.SET_NULL, null=True, blank=True)
    reference = models.ForeignKey(reference, on_delete=models.SET_NULL, null=True, blank=True, related_name="rf_mooe")
    reference_number = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True,blank=True)
    budget_category = models.ForeignKey(budget_category, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'MOOE Data Entry and Monitoring'
    def __str__(self):
        return f"{self.workgroup} - {self.amount}"