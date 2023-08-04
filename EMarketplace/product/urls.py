from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('',views.homeview ,name= 'home'),
    path('<int:id>/', views.product_detail, name='detail'),
    path('<slug:category_slug>/',views.CategoryPage,  name='category'),


]