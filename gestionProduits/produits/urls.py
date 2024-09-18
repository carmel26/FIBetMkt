# produits/urls.py

from django.urls import path, include
from django.contrib.auth import views as auth_views  
# Importation correcte
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'api/produits', ProductViewSet)

urlpatterns = [
    # URLs pour l'API REST
    path('', include(router.urls)),
    
    # URLs pour l'interface web
    path('produits/', ProductListView.as_view(), name='product-list'),
    path('produits/create/', ProductCreateView.as_view(), name='product-create'),
    path('produits/update/<int:pk>/', ProductUpdateView.as_view(), name='product-update'),
    path('produits/delete/<int:pk>/', ProductDeleteView.as_view(), name='product-delete'),
    
    # URLs pour l'authentification
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
]
