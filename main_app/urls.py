from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('vinyls/', views.vinyls_index, name='index'),
    path('vinyls/<int:vinyl_id>/', views.vinyls_detail, name='detail'),
    path('vinyls/create/', views.VinylCreate.as_view(), name='vinyls_create'),
    path('vinyls/<int:pk>/update/', views.VinylUpdate.as_view(), name='vinyls_update'),
    path('vinyls/<int:pk>/delete/', views.VinylDelete.as_view(), name='vinyls_delete'),
    path('vinyls/<int:vinyl_id>/add_photo/', views.add_photo, name='add_photo'),
    # path('accounts/signup/', views.signup, name='signup')
]