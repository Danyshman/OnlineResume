from django.urls import path
from . import views

app_name = 'my_resume'

urlpatterns = [
    path('', views.index, name='index'),
    path('education/', views.education, name='education'),
    path('experience/', views.experience, name='experience'),
    path('skills/', views.skills, name='skills'),
]