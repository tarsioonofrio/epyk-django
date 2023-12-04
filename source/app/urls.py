from django.urls import path

from . import views

urlpatterns = [
    path('dynamic', views.dynamic, name='dynamic'),
    path('views/<str:name>/', views.viewer),
    path('jinja', views.index, name='index'),
    path('chart', views.chart, name='chart'),
]
