from django.urls import path

from goods import views
app_name = 'goods'

urlpatterns = [
    path('', views.shop, name='goods'),
    path('<slug:slug>/', views.shop, name='category')
]
