from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('item/<id>/', views.get_item, name='get_item'),
    # path('config/', views.stripe_config),
    # path('buy/<id>/', views.buy),
]