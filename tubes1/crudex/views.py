from django.shortcuts import render, redirect
from crudex.models import Product
from crudex.forms import ProductForm

# Create your views here.
def index(request):
    products_from_db = Product.objects.all()
    form = ProductForm()
    context_dict={'products_from_context': products_from_db, 'form':form}
    if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save(commit=True)
                return render(request, 'crudex/index.html', context_dict)
            else:
                print(form.errors)
        
    return render (request, 'crudex/index.html', context_dict)

def delete(request,del_product):
    products_from_db = Product.objects.all()
    form = ProductForm()
    context_dict={'products_from_context': products_from_db, 'form':form}
    if request.method == 'POST':
        del_product= Product.objects.get(product_value= del_product)
        del_product.delete()
    return render(request, 'crudex/index.html', context_dict)

def update(request,update_product):
    products_from_db = Product.objects.all()
    form = ProductForm()
    context_dict={'products_from_context': products_from_db, 'form':form}
    if request.method == 'POST':
        update_product= Product.objects.get(product_value= update_product)
        update_product.update()
    return render(request, 'crudex/index.html', context_dict)

