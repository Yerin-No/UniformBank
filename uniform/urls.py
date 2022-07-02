from django.urls import path

from uniform.views import UniformListView

app_name = 'uniform'

urlpatterns = [
    path('list/', UniformListView.as_view(), name='list')   # uniform:list
]