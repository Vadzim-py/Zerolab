from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages


class ListViewMixin(ListView):
    paginate_by = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        items = self.get_queryset().order_by('id')
        paginator = Paginator(items, self.paginate_by)

        page = self.request.GET.get('page')
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)
        context[self.context_object_name] = items
        return context


class CreateObjectMixin(CreateView):
    model = None
    form_class = None
    template_name = None
    success_url = None

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'{self.model.__name__} created successfully.')
        return response


class UpdateObjectMixin(UpdateView):
    model = None
    form_class = None
    template_name = None
    success_url = None

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'{self.model.__name__} updated successfully.')
        return response


class DeleteObjectMixin(DeleteView):
    model = None
    success_url = None

    def form_valid(self, form):
        messages.success(self.request, f'{self.model.__name__} deleted successfully.')
        return super().form_valid(form)
