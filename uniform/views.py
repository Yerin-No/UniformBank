from django.shortcuts import render
from django.views.generic import ListView

from uniform.models import Uniform


class UniformListView(ListView):
    model = Uniform
    # uniform_list.html, {'uniform_list': Uniform.objects.all()}
