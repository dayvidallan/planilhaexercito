from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse

from utils.decorators import LoginRequiredMixin,  StaffRequiredMixin

from .models import Triagem


class TriagemListView(LoginRequiredMixin,  ListView):
    model = Triagem
    
class TriagemMinhasUnidadesListView(LoginRequiredMixin,  ListView):
    model = Triagem
    template_name = 'triagem/unidades_list.html'


class TriagemCreateView(LoginRequiredMixin, CreateView):
    model = Triagem
    fields = ['responsavel', 'unidade', 'categoria', 'paciente', 'data_nascimento', 'altura', 'peso',
              'prec', 'pront', 'proncedimento', 'cdm', 'valor',
              'rx', 'urgencia', 'alta']
    success_url = 'triagem_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Triagem regustrada com sucesso na plataforma!')
        return reverse(self.success_url)


class TriagemUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Triagem
    fields = ['responsavel', 'unidade', 'categoria', 'paciente', 'data_nascimento', 'altura', 'peso',
              'prec', 'pront', 'proncedimento', 'cdm', 'valor',
              'rx', 'urgencia', 'alta']
    success_url = 'triagem_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Dados da triagem atualizados com sucesso na plataforma!')
        return reverse(self.success_url)


class TriagemDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Triagem
    success_url = 'triagem_list'

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL. If the object is protected, send an error message.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            self.object.delete()
        except Exception as e:
            messages.error(request, 'H?? depend??ncias ligadas a essa triagem, permiss??o negada!')
        return redirect(self.success_url)