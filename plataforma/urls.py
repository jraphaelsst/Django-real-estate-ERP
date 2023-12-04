from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('imovel/<str:id>', views.imovel, name='imovel'),
    path('agendar_visita', views.agendar_visita, name='agendar_visita'),
    path('agendamentos', views.agendamentos, name='agendamentos'),
    path('finalizar_agendamento/<str:id>', views.finalizar_agendamento, name='finalizar_agendamento'),
    path('cancelar_agendamento/<str:id>', views.cancelar_agendamento, name='cancelar_agendamento'),
    path('apagar_agendamento/<str:id>', views.apagar_agendamento, name='apagar_agendamento'),
] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)