from django.urls import path
from .views import submit, index, result

urlpatterns = [
    path('', index, name='index'),
    path('submit/', submit, name='submit'),
    path('result/<str:status>/<int:person_id>/', result, name='result'),  # Updated URL pattern
]

