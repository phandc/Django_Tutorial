from django.urls import path

from . import views


#Register namespace
#app_name = "name"

urlpatterns = [
    path('', views.index, name='index' ),
    path('update/<str:pk>', views.updateTask, name='update'),
    path('delete/<str:pk>', views.delete, name='delete')
]