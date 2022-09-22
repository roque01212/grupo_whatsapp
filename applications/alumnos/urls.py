from django.urls import path
from . import views

app_name='alumno_app'

urlpatterns = [
    path('', views.AlumnoView.as_view(), name='Alumno'),
    path('created/', views.AlumnoCreateView.as_view(), name='Created'),
    path('list/', views.AlumnoListView.as_view(), name='List'),
    path('detail/<pk>/', views.AlumnoDetailView.as_view(), name='Detail'),
    path('update/<pk>/', views.AlumnoUpdateView.as_view(), name='Update'),
    path('delete/<pk>/', views.AlumnoDeleteView.as_view(), name='Delete'),
]
