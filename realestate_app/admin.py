from django.contrib import admin

# Register your models here.
# the dot in front of models tells Django to look for 
# models.py in shte same directory as admin.py
from .models import Contract
from .models import ContractActions
from .models import Person
from .models import Transaction

# this tells Django to manage our model through the admin site
admin.site.register(Contract)
admin.site.register(ContractActions)
admin.site.register(Person)
admin.site.register(Transaction)