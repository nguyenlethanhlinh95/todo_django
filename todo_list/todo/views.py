from .models import Todo
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .forms import TodoFormCreate, TodoFormEdit
from django.contrib import messages
from django.shortcuts import get_object_or_404

# Create your views here.

BASE_VIEW = 'todo/'


class TodoListView(TemplateView):
    template_name = BASE_VIEW + "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Linh'
        all_records = Todo.objects.all()
        paginator = Paginator(all_records, 2)
        page = self.request.GET.get('page')
        context['todos'] = paginator.get_page(page)
        return context


class TodoCreateView(FormView):
    model = Todo
    form_class = TodoFormCreate
    template_name = BASE_VIEW + 'create.html'
    success_url = reverse_lazy('todo:index')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Todo created successfully.')
        return super().form_valid(form)


class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoFormEdit
    template_name = BASE_VIEW + 'edit.html'
    success_url = reverse_lazy('todo:index')

    def form_valid(self, form):
        messages.success(self.request, 'Todo updated successfully!')
        return super().form_valid(form)

    def get_object(self):
        id = self.kwargs.get('pk')
        todo = get_object_or_404(Todo, id=id)
        return todo



class TodoDeleteView(DeleteView):
    model = Todo
    template_name = BASE_VIEW + 'delete.html'
    success_url = reverse_lazy('todo:index')

    def form_valid(self, form):
        messages.success(self.request, 'Delete todo successfully!')
        return super().form_valid(form)

    def get_object(self):
        id = self.kwargs.get('pk')
        todo = get_object_or_404(Todo, id=id)
        return todo