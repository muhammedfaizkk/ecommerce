from django.urls import path
from . import views
app_name='custromer'
urlpatterns=[    
    path ('home',views.customer_home)
]