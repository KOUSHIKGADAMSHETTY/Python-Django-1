from django.urls import path
from greet import views

urlpatterns = [
    path('andhra-pradesh/', views.andhra_pradesh_festivals, name='andhra_pradesh_festivals'),
    path('arunachal-pradesh/', views.arunachal_pradesh_festivals, name='arunachal_pradesh_festivals'),
    path('assam/', views.assam_festivals, name='assam_festivals'),
    path('bihar/', views.bihar_festivals, name='bihar_festivals'),
    path('chhattisgarh/', views.chhattisgarh_festivals, name='chhattisgarh_festivals'),
    path('goa/', views.goa_festivals, name='goa_festivals'),
    path('gujarat/', views.gujarat_festivals, name='gujarat_festivals'),
    path('haryana/', views.haryana_festivals, name='haryana_festivals'),
    path('himachal-pradesh/', views.himachal_pradesh_festivals, name='himachal_pradesh_festivals'),
    path('jharkhand/', views.jharkhand_festivals, name='jharkhand_festivals'),
    path('karnataka/', views.karnataka_festivals, name='karnataka_festivals'),
    path('kerala/', views.kerala_festivals, name='kerala_festivals'),
    path('madhya-pradesh/', views.madhya_pradesh_festivals, name='madhya_pradesh_festivals'),
    path('maharashtra/', views.maharashtra_festivals, name='maharashtra_festivals'),
    path('manipur/', views.manipur_festivals, name='manipur_festivals'),
    path('meghalaya/', views.meghalaya_festivals, name='meghalaya_festivals'),
    path('mizoram/', views.mizoram_festivals, name='mizoram_festivals'),
    path('nagaland/', views.nagaland_festivals, name='nagaland_festivals'),
    path('odisha/', views.odisha_festivals, name='odisha_festivals'),
    path('punjab/', views.punjab_festivals, name='punjab_festivals'),
    path('rajasthan/', views.rajasthan_festivals, name='rajasthan_festivals'),
    path('sikkim/', views.sikkim_festivals, name='sikkim_festivals'),
   
]