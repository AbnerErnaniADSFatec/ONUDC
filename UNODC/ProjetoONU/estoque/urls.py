from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("agencias/", include([
        path("", views.AgenciaListView.as_view(), name = 'agencia-list'),
        path("novo/", views.AgenciaCreateView.as_view(), name = 'agencia-create'),
        path("<int:pk>/", views.AgenciaUpdateView.as_view(), name = 'agencia-update'),
    ])),
    path("depoimentos/", include([
        path("", views.DepoimentosListView.as_view(), name = 'depoimentos-list'),
        path("novo/", views.DepoimentosCreateView.as_view(), name = 'depoimentos-create'),
        path("<int:pk>/", views.DepoimentosUpdateView.as_view(), name = 'depoimentos-update'),
    ])),
    path("psicologos/", include([
        path("", views.PsicologoListView.as_view(), name = 'psicologo-list'),
        path("novo/", views.PsicologoCreateView.as_view(), name = 'psicologo-create'),
        path("<int:pk>/", views.PsicologoUpdateView.as_view(), name = 'psicologo-update'),
    ])),
    path("remover/<int:pk>/<str:app>/<str:model>/", views.GenericDeleteView.as_view(), name = 'generic-delete')
]
