from django.urls import path
from . import views

urlpatterns=[
    path('', views.main_page, name='mainpage'),
    path('movie/<int:id>/', views.detail,name='detail'),
    path('add', views.add, name='add'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('cbvhome',views.movielistview.as_view(), name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.detailview.as_view(),name='cbvdetail'),#pk=primarykey
    path('cbvupdate/<int:pk>/',views.updateview.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.deleteview.as_view(),name='cbvdelete'),
    path('mail',views.mailview,name='mail'),



]