from django.urls import path
from .import views

app_name='eco_admin' 

urlpatterns=[
    path('admin_index',views.admin_index, name ='admin_index'),
    path('approve',views.approve, name='approve')
#     path('views',views.views_seller, name='viewsseller')
]