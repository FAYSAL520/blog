from django.contrib import admin
from django.urls import path
from . import views


admin.site.site_header="Faysal Admin"
admin.site.site_title="Faysal Admin Panel"
admin.site.index_title="Welcome to Faysal Admin Panel"



urlpatterns = [

    path('', views.index, name="index"),
    path('addblog', views.create_post, name="addblog"),
    path('<str:pk>/<str:tit>', views.view, name='view'),
    # path('editblog/<int:pk>', views.edit_post, name='edit'),
    path('contact/', views.contact_view, name='sms'),
]