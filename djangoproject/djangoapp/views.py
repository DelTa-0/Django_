from django.shortcuts import render
from .models import Products,Store
from .forms import productForm
from django.shortcuts import get_object_or_404
# Create your views here.
def all_products(request):
    products=Products.objects.all()
    return render(request,'djangoapp/all_django.html',{'products':products})

def product_detail(request,product_id):
    product=get_object_or_404(Products,id=product_id)
    return render(request,'djangoapp/product_details.html',{'product':product})
    
def store_view(request):
    stores=None
    if request.method=='POST':
        form=productForm(request.POST)
        
        if form.is_valid():
            product=form.cleaned_data['products']
            stores=Store.objects.filter(products=product)
    else:
        form=productForm()


    return render(request,'djangoapp/store.html',{'stores':stores,'form':form})