from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from django.contrib.auth.models import Group
from django.contrib import messages
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.views.generic import ListView

#Local
from users.decorators import unauthenticated_user, allowed_users, admin_only


@login_required(login_url='login')
def home(request):
	title = 'Welcome!!!'
	form = "This is home page"
	context = {
		"title": title,
		"form":form,
	}

	return render(request, "home.html", context)
	#return redirect("/")
	
@login_required(login_url='login')
def fill_details(request):
	#form = LoanRequestCreateForm(request.POST or None)
	forms = LoanRequestCreateForm()
	if request.method == 'POST':
		forms = LoanRequestCreateForm(request.POST)
		###Editing starts here
		if forms.is_valid():
			gender = forms.cleaned_data['gender']
			user= request.user
			married = forms.cleaned_data['married']
			dependents = forms.cleaned_data['dependents']
			education = forms.cleaned_data['education']
			self_employed = forms.cleaned_data['self_employed']
			applicantincome = forms.cleaned_data['applicantincome']
			coapplicantincome = forms.cleaned_data['coapplicantincome']
			loanamount = forms.cleaned_data['loanamount']
			loanamount_term = forms.cleaned_data['loanamount_term']
			credit_history = forms.cleaned_data['credit_history']
			property_area = forms.cleaned_data['property_area']
			Loan.objects.create(
				gender=gender,
				user=user,
				married=married,
				dependents=dependents,
				education=education,
				self_employed=self_employed,
				applicantincome=applicantincome,
				coapplicantincome=coapplicantincome,
				loanamount=loanamount,
				credit_history=credit_history,
				property_area=property_area,
				loan_status='pending'
			)
			messages.success(request, 'Your informations have been received!')
			return redirect('ApplicantPersonalDetails')
	context = {
		'form': forms,
		'title': "Personal information",
		}
		####Editing ends here
	#if form.is_valid():
	# 	form.save()
	# 	messages.success(request, 'Your informations have been received!')
	# 	return redirect('/')
	# context = {
	# 	"form": form,
	# 	"title": "Personal information"
	# }
	return render(request, "add_items.html", context)

class LoanapplicantsListView(ListView):
	model = Loan
	template_name = 'loanApplicants_list.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['loan'] = Loan.objects.all().order_by('-id')
		return context

# class LoanapplicantsPersonalListView(ListView):
# 	model = Loan
# 	template_name = 'ApplicantPersonalDetails.html'

# 	def get_context_data(self, **kwargs):
# 		current_user = user.username
# 		context = super().get_context_data(**kwargs)
# 		context['loan'] = Loan.objects.get(username=current_user)
# 		return context

class LoanapplicantsPersonalListView(ListView):
	model = Loan
	template_name = 'ApplicantPersonalDetails.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['loan'] = Loan.objects.filter(user=self.request.user.id)
		return context

	# def get_queryset(self):
	# 	return Loan.objects.filter(user=self.request.user)
# def LoanapplicantsPersonal(request):
# 	current_user = request.user
# 	User = get_user_model()
# 	user_in_DB = Loan.objects.get(CustomUser.username==current_user)
# 	context = {
# 		"user_in_DB": user_in_DB,
# 		"current_user": current_user,
# 	}

# 	return render (request, "ApplicantPersonalDetails.html", context)