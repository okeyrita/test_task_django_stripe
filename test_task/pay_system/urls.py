from django.urls import path
from . import views


urlpatterns = [
    path('items/', views.start_page, name='items'),
    path('item/<int:pk>', views.item_page, name='item'),
    path('buy/<int:pk>', views.buy_item, name='buy_item'),
]