from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
    path('catalog/', views.CategoryList.as_view(),
         name='category_list'),
    path('catalog/<int:pk>/', views.CategoryDetail.as_view(),
         name='category_detail'),
    path('catalog/<int:category_id>/<int:pk>/',
         views.ProductDetail.as_view(), name='product_detail'),
    path('catalog/category_create/', views.CategoryCreate.as_view(),
         name='category_create'),
    path('catalog/<int:pk>/delete/', views.CategoryDelete.as_view(),
         name='category_delete'),
    path('catalog/product_create/', views.ProductCreate.as_view(),
         name='product_create'),
    path('catalog/product/<int:pk>/delete/', views.ProductDelete.as_view(),
         name='product_delete')
]