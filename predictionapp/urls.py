from django.urls import path, include
from predictionapp import views
from .views import  LoanapplicantsListView , LoanapplicantsPersonalListView

urlpatterns = [
    path('', views.home, name='home'), 
     path('add_items/', views.fill_details, name='add_items'),   
     #path('ApplicantPersonalDetails/', views.LoanapplicantsPersonal, name='ApplicantPersonalDetails'), 

     path('loanApplicants_list/', LoanapplicantsListView.as_view(), name='loanApplicants_list'),
     path('ApplicantPersonalDetails/', LoanapplicantsPersonalListView.as_view(), name='ApplicantPersonalDetails'),
    ]