
from django.urls import path

from shop import views
app_name='shop'
urlpatterns = [
    path('',views.allprodcat,name='allprodcat'),
    path('shop/<slug:c_slug>/',views.allprodcat,name='products_by_category'),
    path('shop/<slug:c_slug>/<slug:p_slug>/',views.product_details,name='products_category_detail')
]
