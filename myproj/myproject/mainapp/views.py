from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import *
from django.urls import reverse_lazy

class IndexPage(TemplateView):
    template_name = 'mainapp/index.html'

class CategoryList(ListView):
    template_name = 'mainapp/category_list.html'
    model = Category

class CategoryDetail(DetailView):
    template_name = 'mainapp/category_detail.html'
    model = Category

class ProductDetail(DetailView):
    template_name = 'mainapp/product_detail.html'
    model = Product

class CategoryCreate(CreateView):
    template_name = 'mainapp/category_create.html'
    model = Category
    fields = ['name']
    success_url = reverse_lazy('mainapp:category_list')

class CategoryDelete(DeleteView):
    template_name = 'mainapp/category_delete.html'
    model = Category
    success_url = reverse_lazy('mainapp:category_list')

class ProductCreate(CreateView):
    template_name = 'mainapp/product_create.html'
    model = Product
    fields = ['name', 'category']
    success_url = reverse_lazy('mainapp:category_list')

class ProductDelete(DeleteView):
    template_name = 'mainapp/product_delete.html'
    model = Product
    success_url = reverse_lazy('mainapp:category_list')