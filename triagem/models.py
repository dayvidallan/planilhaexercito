from __future__ import unicode_literals

from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from unidade.models import Categoria

from utils.gerador_hash import gerar_hash
    
class Triagem(models.Model): 
    #dados do responsável
    responsavel = models.ForeignKey('usuario.Usuario', verbose_name= 'Responsável pela triagem *', on_delete=models.PROTECT, related_name='responsavel')
    unidade = models.ForeignKey('unidade.Unidade', verbose_name= 'Unidade de Atendimento *', on_delete=models.PROTECT, related_name='unidade')
    categoria = models.ForeignKey(Categoria, verbose_name = 'Situação Mil *', on_delete = models.PROTECT, related_name = 'categoria', null = True, blank = True)
    
    #dados do paciente e da consulta
    data = models.DateField(_('Data da triagem '), max_length=10, help_text='Use dd/mm/aaaa')
    hora = models.TimeField(_('Hora da triagem '), max_length=10, help_text='Use hh:mm')
    paciente = models.CharField(_('Informe o nome completo do paciente *'), max_length=100, help_text= '* indica campos obrigatórios')
    data_nascimento = models.DateField(_('Data de nascimento'), max_length=10, help_text='Use dd/mm/aaaa', null=True, blank=True)
    altura = models.DecimalField(_('Altura em metros'), max_digits=3, decimal_places=2, validators=[MinValueValidator(0.0), MaxValueValidator(2.5)], null=True, blank=True)
    peso = models.DecimalField(_('Peso em kg'), max_digits=5, decimal_places=2, validators=[MinValueValidator(0.0), MaxValueValidator(400.0)], null=True, blank=True)
    prec = models.CharField(_('PREC CP'), max_length=150, null=True, blank=True)
    pront = models.CharField(_('Pront'), max_length=150, null=True, blank=True)
    proncedimento = models.TextField(_('Procedimento *'), null=True, blank=True)
    cdm = models.CharField(_('CDM'), max_length=150, null=True, blank=True)
    valor = models.DecimalField(_('VALOR (R$)'), max_digits=5, decimal_places=2, validators=[MinValueValidator(0.0), MaxValueValidator(400.0)], null=True, blank=True)

    #dados da triagem
    rx = models.BooleanField(_('Teve RX ?'), default=False)
    urgencia = models.BooleanField(_('É Urgente?'), default=False)
    alta = models.BooleanField(_('Teve Alta?'), default=False)
    slug = models.SlugField('Hash',max_length= 200, null=True, blank=True)
    
    objects = models.Manager()
    
    class Meta:
        ordering            =   ['-data', '-hora', 'paciente']
        verbose_name        =   ('triagem')
        verbose_name_plural =   ('triagenss')
        unique_together     =   [['data','hora','paciente']]

    #def __str__(self):
        #return "Paciente: %s. Resultado: %s." % (self.paciente, self.resultado_literal_triagem)

    def save(self, *args, **kwargs):
        self.paciente = self.paciente.upper()
        
        self.data = datetime.now()
        self.hora = datetime.now()
        
        if not self.slug:
            self.slug = gerar_hash()
        super(Triagem, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse('triagem_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('triagem_delete', args=[str(self.id)]) 

    @property
    def idade(self):
        return  datetime.now().year - self.data_nascimento.year
    
