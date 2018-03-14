"""Defines url patterns for learning_logs."""

from django.urls import path
from django.conf.urls import url
from .import views

app_name = 'pizzas'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    
    # Show all pizzas.
    #path('pizzas/', views.pizzas, name='pizzas'),
    
    # Detail page for a single topic.
    #path('pizzas/<int:pizzas_id>/', views.pizzas, name='pizzas'),
    url(r'^pizzas/$', views.pizzas, name='pizzas'),
    
    # Detail page for a single topic.
    url(r'^topping/$', views.topping, name='topping'),
        
    #order pizza    
    path(r'order/', views.order, name='order'),
    
    #contact form
    url(r'^contact/$', views.contact, name='contact'),
    
    #stripe payment
    #url(r'^charge/$', views.charge, name='charge'),
]
