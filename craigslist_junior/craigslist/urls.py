from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('new-cat', views.new_category, name='new_category'),
    path('<int:category_id>/new-item', views.new_item, name='new_item'),
    path('<int:category_id>', views.category_items, name='category_items'),
    path('<int:category_id>/<int:item_id>', views.item_detail, name='item_detail'),
    path('<int:category_id>/edit', views.edit_category, name='edit_category'),
    path('<int:category_id>/<int:item_id>/edit', views.edit_item, name='edit_item'),
    path('<int:category_id>/delete', views.delete_category, name='delete_category'),
    path('<int:category_id>/<int:item_id>/delete', views.delete_item, name='delete_item'),
]