from django.urls import path
from main_app.views import home, service, welcome, generate_pdf, generate_pdf_file, generate_csv
from . import views

urlpatterns = [
    path('',home,name='home_page'),
    path('service/',service,name='service'),
    path('welcome/',welcome,name='welcome'),
    path('generate-pdf/',generate_pdf,name='generate_pdf'),
    path('generate-csv/', views.generate_csv, name='generate_csv'),
]
