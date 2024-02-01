from django.urls import path
from main_app.views import home, service, welcome

urlpatterns = [
    path('',home,name='home_page'),
    path('service/',service,name='service'),
    path('welcome/',welcome,name='welcome')
]
