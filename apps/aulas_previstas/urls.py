"""app aulas_previstas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from apps.aulas_previstas import views

app_name = 'aulas_previstas'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('resultados/', views.show_results, name='show_results'),
    path('ajax/load-feriados/', views.load_feriados, name='ajax_load_feriados'),
    path('ajax/load-fim-ano/', views.load_fim_ano, name='ajax_load_fim_ano'),
    path('ajax/load-inicio-ano/', views.load_inicio_ano, name='ajax_load_inicio_ano'),
]
