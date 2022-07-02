from django.urls import path

from uniform.views import UniformListView, UniformCreateView, UniformDetailView, UniformUpdateView, UniformDeleteView

app_name = 'uniform'

urlpatterns = [
    path('list/', UniformListView.as_view(), name='list'),   # uniform:list
    path('add/', UniformCreateView.as_view(), name='add'),  # uniform:add
    path('detail/<int:pk>/', UniformDetailView.as_view(), name='detail'),   # uniform:detail
    path('edit/<int:pk>/', UniformUpdateView.as_view(), name='edit'),   # bookmark:edit
    path('delete/<int:pk>/', UniformDeleteView.as_view(), name='delete'),  # bookmark:delete
]