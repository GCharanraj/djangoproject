from django.urls import path
from babu import views

urlpatterns=[
    path('',views.func,name='sname'),
    path('strong',views.func2,name='arm_strong num')
]