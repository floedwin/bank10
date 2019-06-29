# Generated by Django 2.0.5 on 2018-06-05 08:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyConverter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('currency', models.CharField(default=0, max_length=200)),
                ('amount_UGX', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerBankaccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='', max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('contact', models.IntegerField(default=0)),
                ('residence', models.CharField(default='', max_length=200)),
                ('work_history', models.CharField(default='', max_length=200)),
                ('identification_information', models.IntegerField(default=0)),
                ('next_of_kin', models.CharField(default='', max_length=200)),
                ('relationship', models.CharField(default='', max_length=200)),
                ('account_number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='LoanCalculator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('loan_period', models.CharField(default='', max_length=200)),
                ('interest_rate', models.IntegerField(default=0)),
                ('results', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Registercustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=200)),
                ('last_name', models.CharField(default='', max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('contact', models.IntegerField(default=0)),
                ('residence', models.CharField(default='', max_length=200)),
                ('occupation', models.CharField(default='', max_length=200)),
                ('next_of_kin', models.CharField(default='', max_length=200)),
                ('relationship', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Registercustomertranscations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_name', models.CharField(default='', max_length=200)),
                ('Email', models.EmailField(blank=True, max_length=254)),
                ('Contact', models.IntegerField(default=0)),
                ('Account_number', models.IntegerField(default=0)),
                ('Transcation_type', models.CharField(default='', max_length=200)),
                ('Amount', models.IntegerField(default=0)),
                ('Transcation_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
