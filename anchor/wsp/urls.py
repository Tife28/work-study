from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('show', views.show, name='show'),
    path('trys', views.trys, name='trys'),
    path('edit/<int:id>', views.edit, name='edit'),  
    path('update/<int:id>', views.update, name='update'),  
    path('delete/<int:id>', views.destroy, name='delete'), 
]
