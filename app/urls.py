from django.urls import path
from . import views

handler404 = 'app.views.custom_404_view'
handler500 = 'app.views.custom_500_view'

urlpatterns = [
    path('', views.home, name='home'),
    path('services', views.services, name='services'),
    path('demo', views.demo, name='demo'),
    path('legal', views.legal, name='legal'),
    path('login', views.login, name='login'),
    path('careers', views.careers, name='careers'),
    path('about', views.about, name='about'),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('pricing/', views.pricing, name='pricing'),
    # path('chart/', views.chart, name='chart'),
    # path('upload-csv/', views.upload_csv_view, name='upload_csv'),

]