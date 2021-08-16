from django.urls import path
from . import views
urlpatterns = [
    path('search', views.search_view, name='search'),
    path('', views.index_view, name='listings'),
    path('<int:listing_id>', views.listing_view, name='listing'),
]