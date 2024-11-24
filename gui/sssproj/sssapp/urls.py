from django.urls import path
from . import views

urlpatterns = [
    path('diagnose/', views.diagnose_patient, name='diagnose_patient'),
    path('index/',views.index, name='index'),
]
