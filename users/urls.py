from django.urls import path, include
from . import views

urlpatterns = [

    path('',views.index, name='index'),
    path('employee_detail/', views.employee_detail, name='employee_detail'),

    path('employee_detail/<int:id>', views.employee_detail, name='employee_detail'),
    # path('simple_details/', views.simple_details, name='simple_details'),

]