from django.apps import apps
from django.db.models import Avg
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic.edit import FormMixin
from django.views.generic.edit import ModelFormMixin

from estoque.models import Agencia, Depoimentos, Psicologo

def index(request):
    return render(request, 'estoque/index.html')

class GenericDeleteView(DeleteView):
    model = None
    template_name = 'estoque/confirm_delete.html'

    def get_object(self):
        ModelClass = apps.get_model(
            app_label=self.kwargs['app'],
            model_name=self.kwargs['model']
        )
        obj = get_object_or_404(ModelClass, pk=self.kwargs['pk'])
        return obj

    def get_success_url(self):
        return self.request.GET.get('success_url', '/')

class JsonListMixin(object):
    json_fields = []

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset().values_list(*self.json_fields)
        json_dict = {
            'header': self.json_fields,
            'object_list': list(self.object_list)
        }
        return JsonResponse(json_dict)


class PageInfoMixin(object):
    page_info = None

    def get_page_info(self):
        if self.model:
            return {
                'page_info': self.model._meta.verbose_name,
                'page_info_plural': self.model._meta.verbose_name_plural,
            }
        return None

    def get_context_data(self, **kwargs):
        if self.page_info is None:
            kwargs.update(self.get_page_info())
        return super().get_context_data(**kwargs)

#================================================= Agencia Operacao =======================================================#

class AgenciaListView(PageInfoMixin, ModelFormMixin, ListView):
    model = Agencia
    fields = '__all__'

    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)


class AgenciaCreateView(PageInfoMixin, CreateView):
    model = Agencia
    fields = '__all__'
    success_url = reverse_lazy('agencia-list')

    def form_valid(self, form):
        if self.request.is_ajax():
            obj = form.save()
            return JsonResponse({
                'obj': {
                    'nome': obj.nome,
                    'idade': obj.idade,
                }
            })
        else:
            return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({
                'errors': form.errors,
                'non_field_errors': form.non_field_errors()
            })
        else:
            return super().form_invalid(form)


class AgenciaUpdateView(PageInfoMixin, UpdateView):
    model = Agencia
    fields = '__all__'
    success_url = reverse_lazy('agencia-list')

#================================================= Depoimentos =======================================================#

class DepoimentosListView(PageInfoMixin, ListView):
    model = Depoimentos
    fields = '__all__'

    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)


class DepoimentosCreateView(PageInfoMixin, CreateView):
    model = Depoimentos
    fields = '__all__'
    success_url = reverse_lazy('depoimentos-list')


class DepoimentosUpdateView(PageInfoMixin, UpdateView):
    model = Depoimentos
    fields = '__all__'
    success_url = reverse_lazy('depoimentos-list')

#================================================= Psicologo =======================================================#

class PsicologoListView(PageInfoMixin, ModelFormMixin, ListView):
    model = Psicologo
    fields = '__all__'

    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)

class PsicologoCreateView(PageInfoMixin, CreateView):
    model = Psicologo
    fields = '__all__'
    success_url = reverse_lazy('psicologo-list')


class PsicologoUpdateView(PageInfoMixin, UpdateView):
    model = Psicologo
    fields = '__all__'
    success_url = reverse_lazy('psicologo-list')
