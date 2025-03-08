from django.urls import path
from . import views

urlpatterns = [
    path('', views.ADD),
    path('EDIT/', views.EDIT),
    path('addstudent/', views.addstudent),
    path('editstudent/<int:id>/', views.editstudent),
    path('editstudent/<int:id>/updatestudent/', views.updatestudent),
    path('deletestudent/<int:id>/', views.deletestudent)
]