from django.contrib import admin

from .models import Registercustomer,Registercustomertranscations,CustomerBankaccount,LoanCalculator,CurrencyConverter

admin.site.register(Registercustomer)
admin.site.register(Registercustomertranscations)
admin.site.register(CustomerBankaccount)
admin.site.register(LoanCalculator)
admin.site.register(CurrencyConverter)
admin.site.site_header ='Administration'
