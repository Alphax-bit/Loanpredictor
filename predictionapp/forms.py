from django import forms
from .models import *

class LoanRequestCreateForm(forms.ModelForm):
	class Meta:
		model = Loan
		fields = ['gender','user', 'married', 'dependents', 'education', 
        'self_employed', 'applicantincome', 'coapplicantincome', 
        'loanamount', 'loanamount_term', 'credit_history', 'property_area']