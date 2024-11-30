from django.urls import path
from . import views

urlpatterns = [
    # path('diagnose/', views.diagnose_patient, name='diagnose_patient'),
    path('',views.predict, name='predict'),
]
