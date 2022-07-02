from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from uniform.models import Uniform


class UniformListView(ListView):
    model = Uniform
    # uniform_list.html, {'uniform_list': Uniform.objects.all()}


class UniformCreateView(CreateView):
    model = Uniform
    fields = ['name', 'size']       # '__all__'
    template_name_suffix = '_create'    # uniform_form.html -> uniform_create.html
    success_url = reverse_lazy('uniform:list')


class UniformDetailView(DetailView):
    model = Uniform


class UniformUpdateView(UpdateView):
    model = Uniform
    fields = ['name', 'size']  # '__all__'
    template_name_suffix = '_update'  # bookmark_update.html
    # success_url = reverse_lazy('bookmark:list')   #success_url 없으면 model의 get_absolute_url() 호출


class UniformDeleteView( DeleteView):
    model = Uniform
    success_url = reverse_lazy('uniform:list')
