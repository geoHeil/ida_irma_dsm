from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.ida_home, name='ida_home'),
	path('ida_add_internal_microdata', views.ida_add_internal_microdata, name='ida_add_internal_microdata'),
	path('irma_home', views.irma_home, name='irma_home'),
	path('dsm_home', views.dsm_home, name='dsm_home'),

]
