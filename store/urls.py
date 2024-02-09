from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [

    path('',views.store,name='store'),
    path('offers/',views.offer,name='offer'),
    path('<str:category_slug>/',views.store,name='category_slug'),

    path('<str:category_slug>/<str:product_slug>/',views.product_detail,name='product_detail'),
  
]
