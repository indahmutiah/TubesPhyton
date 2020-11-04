from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('del/<slug:del_product>', views.delete),
    path('update/<slug:update_product>', views.update),
]