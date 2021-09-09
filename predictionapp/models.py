from django.db import models

from users.models import CustomUser

class Loan(models.Model):


	EDUCATION_CHOICES = [
	('Graduate', 'Graduate'),
	('Not Graduate', 'Not Graduate'),
	]
   
	PROPERTY_AREA_CHOICES = [
	('Urban', 'Urban'),
	('Rural', 'Rural'),
	]
   
	GENDER_CHOICES = [
	('Male', 'Male'),
	('Female', 'Female'),
	]
   
	MARRIED_CHOICES = [
	('Yes', 'Yes'),
	('No', 'No'),
	]
   
	SELF_EMPLOYED_CHOICES = [
	('Yes', 'Yes'),
	('No', 'No'),
	]
   
	LOAN_STATUS_CHOICES = [
	    ('pending', 'Pending'),
        ('decline', 'Decline'),
        ('approved', 'Approved'),
        ('processing', 'Processing'),
        ('complete', 'Complete'),
	]

	gender = models.CharField(max_length=50, blank=False, null=False, choices=GENDER_CHOICES)
	user = models.ForeignKey(CustomUser, null=True, default = "", on_delete=models.CASCADE)
	married = models.CharField(max_length=50, blank=False, null=False, choices=MARRIED_CHOICES)
	dependents = models.IntegerField(default='0', blank=False, null=False)
	education = models.CharField(max_length=50, blank=False, null=False, choices=EDUCATION_CHOICES)
	self_employed = models.CharField(max_length=50, blank=False, null=False, choices=SELF_EMPLOYED_CHOICES)
	applicantincome = models.IntegerField(default='0', blank=False, null=True)
	coapplicantincome = models.IntegerField(default='0', blank=False, null=True)
	loanamount = models.IntegerField(default='0', blank=False, null=True)
	loanamount_term = models.IntegerField(default='0', blank=False, null=True)
	credit_history = models.IntegerField(default='1', blank=False, null=True)
	property_area = models.CharField(max_length=50, blank=False, null=False, choices=PROPERTY_AREA_CHOICES)
	loan_status = models.CharField(max_length=50, blank=False, null=False, choices=LOAN_STATUS_CHOICES)

	def __str__(self):
		return self.gender + '' + str(self.loanamount)
  