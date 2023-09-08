from .views import *
from django.urls import path

urlpatterns = [
    path('home/',HomeView.as_view(),name='home'),
    path('index/',IndexView.as_view(),name='index'),
    path('create-components/',ComponentsView.as_view(),name="create-components"),
    path('get-components/',ComponentsListView.as_view(),name="get-components"),
    path('components-update/<int:id>/',ComponentsEditView.as_view(),name="components_update"),
    path('create-groups/',GroupView.as_view(),name="create-groups"),
    # path('components-list/',ComponentsListView.as_view(),name="components-list"),
    
]