# produits/views.py

from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from .forms import ProductForm
# produits/views.py

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


# Vues pour l'interface web

# Vue pour lister les produits
class ProductListView(ListView):
    model = Product
    template_name = 'produits/product_list.html'
    context_object_name = 'produits'

# Vue pour créer un nouveau produit
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'produits/product_form.html'
    success_url = reverse_lazy('product-list')

# Vue pour mettre à jour un produit existant
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'produits/product_form.html'
    success_url = reverse_lazy('product-list')

# Vue pour supprimer un produit
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'produits/product_confirm_delete.html'
    success_url = reverse_lazy('product-list')

# ViewSet pour l'API REST

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
