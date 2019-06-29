from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from boards.models import  Registercustomer,CustomerBankaccount,Registercustomertranscations,LoanCalculator,CurrencyConverter
from . import  models
# Create your views here.
def home(request):
    return render(request, 'home.html')
def about_us(request):
    return  render(request,'about_us.html')
def contact(request):
    return  render(request,'contact.html')
def my_account(request):
    return render(request,'my_account.html')
def business_loans_and_leases(request):
    return render(request,'business_loans_and_leases.html')
def consumer_loans(request):
    return  render(request,'consumer_loans.html')
def special_loan_schemes(request):
    return  render(request,'special_loan_schemes.html')
def solar_loans(request):
    return  render(request,'solar_loans.html')
def home_improvement_loans(request):
    return  render(request,'home_improvement_loans.html')
def agricultural_loans(request):
    return  render(request,'agricultural_loans.html')
def bank_over_draft(request):
    return  render(request,'bank_over_draft.html')
def trade_finance(request):
    return  render(request,'trade_finance.html')
def micro_business_loans(request):
    return  render(request,'micro_business_loans.html')
def savings_account(request):
    return  render(request,'savings_account.html')
def current_account(request):
    return  render(request,'current_account.html')
def cente_fixed_deposit_account(request):
    return  render(request,'cente_fixed_deposit_account.html')
def ATM_services(request):
    return  render(request,'ATM_services.html')
def ATM_cardless_withdraw(request):
    return  render(request,'ATM_cardless_withdraw.html')
def cente_point(request):
    return  render(request,'cente_point.html')
def Ewater_payments(request):
    return  render(request,'Ewater_payments.html')
def airtel_money(request):
    return  render(request,'airtel_money.html')
def MTN_mobile_money_transfer(request):
    return  render(request,'MTN_mobile_money_transfer.html')
def western_union_money_transfer(request):
    return  render(request,'western_union_money_transfer.html')
def platinum_banking(request):
    return  render(request,'platinum_banking.html')
def school_fees_payment_services(request):
    return  render(request,'school_fees_payment_services.html')
def standing_orders(request):
    return  render(request,'standing_orders.html')
def currency_rates(request):
    return  render(request,'currency_rates.html')


class RegisterCustomer(TemplateView):
    template_name = 'RegisterCustomer.html'
    def get(self,request):
        customers = Registercustomer.objects.filter(first_name='Florence')
        args = {'customers': customers}
        return render(request,self.template_name, args)
class CustomerBankAccount(TemplateView):
    template_name = 'CustomerBankAccount.html'

    def get(self, request):
        accounts = CustomerBankaccount.objects.all()
        args = {'accounts': accounts}
        return  render(request,self.template_name,args)


class RegisterCustomerTranscations(TemplateView):
    template_name = 'RegisterCustomerTranscations.html'

    def get(self, request):
        transactions = Registercustomertranscations.objects.all()

        args = {'transactions': transactions}
        return render(request, self.template_name, args)
class loan_calculator(TemplateView):
    template_name = 'loan_calculator.html'

    def get(self, request):
        loans= LoanCalculator.objects.all()
        args = {'loans': loans}
        return  render(request,self.template_name,args)
class currency_converter(TemplateView):
    template_name = 'currency_converter.html'

    def get(self, request):
        currencies= CurrencyConverter.objects.all()
        args = {'currencies': currencies}
        return  render(request,self.template_name,args)
