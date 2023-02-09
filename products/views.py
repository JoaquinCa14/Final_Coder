from django.shortcuts import render
from django.http import HttpResponse

from products.models import Products
from products.forms import ProductForms

def create_product(request):
    if request.method =='GET':

        context =  {
            'form': ProductForms()
        }

        return render(request, 'products/create_product.html', context=context)

    elif request.method =='POST': 
        form = ProductForms(request.POST)
        if form.is_valid():
            Products.objects.create(
                name=form.cleaned_data['name'],
                price=form.cleaned_data['price'],
                stock=form.cleaned_data['stock'],
            )
            context = {
                'message': 'Producto creado exitosamente'
            }
            return render(request, 'products/create_product.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': ProductForms()

            }
            
        return render(request, 'products/create_product.html', context=context)

    

def list_products(request):
    if 'search' in request.GET:
        search = request.GET['search']
        products = Products.objects.filter(name__icontains=search) 
    else:
        products = Products.objects.all()
    context = {
        'products': products,
    }

    return render (request, 'list_products.html', context=context)

