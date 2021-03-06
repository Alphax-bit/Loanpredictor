# Generated by Django 3.2.6 on 2021-09-06 11:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('predictionapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='user',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='loan',
            name='applicantincome',
            field=models.IntegerField(default='0', null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='coapplicantincome',
            field=models.IntegerField(default='0', null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='credit_history',
            field=models.IntegerField(default='1', null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='dependents',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='education',
            field=models.CharField(choices=[('Graduate', 'Graduate'), ('Not Graduate', 'Not Graduate')], max_length=50),
        ),
        migrations.AlterField(
            model_name='loan',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50),
        ),
        migrations.AlterField(
            model_name='loan',
            name='loan_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('decline', 'Decline'), ('approved', 'Approved'), ('processing', 'Processing'), ('complete', 'Complete')], max_length=50),
        ),
        migrations.AlterField(
            model_name='loan',
            name='loanamount',
            field=models.IntegerField(default='0', null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='loanamount_term',
            field=models.IntegerField(default='0', null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='married',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=50),
        ),
        migrations.AlterField(
            model_name='loan',
            name='property_area',
            field=models.CharField(choices=[('Urban', 'Urban'), ('Rural', 'Rural')], max_length=50),
        ),
        migrations.AlterField(
            model_name='loan',
            name='self_employed',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=50),
        ),
    ]
