from django.urls import path

from . import views

app_name = 'report_fault'

urlpatterns = [
    path('', views.report_a_fault, name='report'),
]
