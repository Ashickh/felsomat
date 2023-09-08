from django.db import models

# Create your models here.

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=30, null=True, blank=True)
    base_quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=8,decimal_places=2)
    total_cost = models.DecimalField(max_digits=8,decimal_places=2)
    alias = models.CharField(max_length=200, null=True, blank=True)
    remarks = models.CharField(max_length=200, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


class Assembly(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=30, null=True, blank=True)
    base_quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=8,decimal_places=2)
    total_cost = models.DecimalField(max_digits=8,decimal_places=2)
    alias = models.CharField(max_length=200, null=True, blank=True)
    remarks = models.CharField(max_length=200, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

class AssemblyDetail(models.Model):
    id = models.AutoField(primary_key=True)
    assembly_id = models.ForeignKey(Assembly, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    
    def __str__(self):
        return f"{self.assembly} - {self.item}"
