"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import  path
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views
from blog  import feed

from boards import views
from boards.views import  RegisterCustomer,CustomerBankAccount,RegisterCustomerTranscations,loan_calculator,currency_converter
urlpatterns = [
     url(r'^blog/', include('blog.urls')),
    url(r'^feed/$',feed.LatestPosts(), name="feed"),
    url(r'^$', views.home, name='home'),
    url(r'^about_us/$', views.about_us, name='about_us'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^my_account/$', views.my_account, name='my_account'),
    url(r'^business_loans_and_leases/$', views.business_loans_and_leases, name='business_loans_and_leases'),
    url(r'^consumer_loans/$', views.consumer_loans, name='consumer_loans'),
    url(r'^special_loan_schemes/$', views.special_loan_schemes, name='special_loan_schemes'),
    url(r'^solar_loans/$', views.solar_loans, name='solar_loans'),
    url(r'^home_improvement_loans/$', views.home_improvement_loans, name='home_improvement_loans'),
    url(r'^agricultural_loans/$',views.agricultural_loans,name='agricultural_loans'),
    url(r'^bank_over_draft/$',views.bank_over_draft,name='bank_over_draft'),
    url(r'^trade_finance/$',views.trade_finance,name='trade_finance'),
    url(r'^micro_business_loans/$',views.micro_business_loans,name='micro_business_loans'),
    url(r'^RegisterCustomer/$', RegisterCustomer.as_view(), name='RegisterCustomer'),
    url(r'^CustomerBankAccount/$', CustomerBankAccount.as_view(), name='CustomerBankAccount'),
    url(r'^current_account/$', views.current_account, name='current_account'),
    url(r'^currency_rates/$', views.currency_rates, name='currency_rates'),
    url(r'^savings_account/$', views.savings_account, name='savings_account'),
    url(r'^ATM_services/$', views.ATM_services, name='ATM_services'),
    url(r'^ATM_cardless_withdraw/$', views.ATM_cardless_withdraw, name='ATM_cardless_withdraw'),
    url(r'^cente_point/$', views.cente_point, name='cente_point'),
    url(r'^Ewater_payments/$', views.Ewater_payments, name='Ewater_payments'),
    url(r'^airtel_money/$', views.airtel_money, name='airtel_money'),
    url(r'^MTN_mobile_money_transfer/$', views.MTN_mobile_money_transfer, name='MTN_mobile_money_transfer'),
    url(r'^western_union_money_transfer/$', views.western_union_money_transfer, name='western_union_money_transfer'),
    url(r'^platinum_banking/$', views.platinum_banking, name='platinum_banking'),
    url(r'^school_fees_payment_services/$', views.school_fees_payment_services, name='school_fees_payment_services'),
    url(r'^standing_orders/$', views.standing_orders, name='standing_orders'),
    url(r'^cente_fixed_deposit_account/$', views.cente_fixed_deposit_account, name='cente_fixed_deposit_account'),
    url(r'^RegisterCustomerTranscations/$', RegisterCustomerTranscations.as_view(),
        name='RegisterCustomerTranscations'),
    url(r'^loan_calculator/$', loan_calculator.as_view(), name='loan_calculator'),
    url(r'^currency_converter/$', currency_converter.as_view(), name='currency_converter'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt'
        ),
        name='password_reset'),
    url(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),

    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'),
    url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'),
    url(r'^settings/account/$', accounts_views.UserUpdateView.as_view(), name='my_account'),
    url(r'^markdown/', include("django_markdown.urls")),
    #path('markdown/', include( 'django_markdown.urls')),
    url(r'^admin/', admin.site.urls),

]