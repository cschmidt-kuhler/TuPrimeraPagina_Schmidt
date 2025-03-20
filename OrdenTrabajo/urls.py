from django.urls import path
from .views import saludo, lista_operarios, detalle_operario


urlpatterns = [ path('saludo/', saludo), 
                path('operarios', lista_operarios, name='lista_operarios'),
                path('operarios/<int:pk>/', detalle_operario, name='detalle_operario'),
    ]