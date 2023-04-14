from django.urls import path
from .views import dropdown,  medicine_results

urlpatterns = [
    path('', dropdown, name='dropdown'),
    path('medicine-results/', medicine_results, name='medicine_results'),
]
