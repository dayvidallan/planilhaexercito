from django.conf.urls import url

from .views import UnidadeListView, UnidadeCreateView, CategoriaListView, CategoriaCreateView
from .views import UnidadeUpdateView, UnidadeDeleteView, CategoriaUpdateView, CategoriaDeleteView


urlpatterns = [
	url(r'list/$', UnidadeListView.as_view(), name='unidade_list'),
	url(r'cad/$', UnidadeCreateView.as_view(), name='unidade_create'),
	url(r'(?P<pk>\d+)/$', UnidadeUpdateView.as_view(), name='unidade_update'),
	url(r'(?P<pk>\d+)/delete/$', UnidadeDeleteView.as_view(), name='unidade_delete'),
	#Categoria
	url(r'listcat/$', CategoriaListView.as_view(), name='categoria_list'),
	url(r'categoria/$', CategoriaCreateView.as_view(), name='categoria_create'),
	url(r'(?P<pk>\d+)/update/$', CategoriaUpdateView.as_view(), name='categoria_update'),
	url(r'(?P<pk>\d+)/deletar/$', CategoriaDeleteView.as_view(), name='categoria_delete'),

]
