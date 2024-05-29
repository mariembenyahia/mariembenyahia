from django.urls import path
from . import views
urlpatterns = [


    path('signup/' ,views.SignupPage,name='SignupPage'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profil/', views.profil, name='profil'),
    path('loginoperateur/',views.login_view2,name='login_view2'),
    path('dashboardop/',views.dashboardop,name='dashboardop'),
    path('Customers/',views.Customers,name='Customers'),
    path('profilop/', views.profilop, name='profilop'),
    path('fortigate/', views.fortigate, name='fortigate'),  
    path('routestatic/', views.routestatic, name='routestatic'),
    path('sdwan/', views.sdwan, name='sdwan'),
    path('firewall/', views.firewall, name='firewall'),
    path('login/', views.login_fortigate, name='login_fortigate'),
]

