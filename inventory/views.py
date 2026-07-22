from django.shortcuts import render, redirect,get_object_or_404
from .models import Product
from .forms import ProductForm
#home
def home(request):
    return render(render,"home.html")
#productlist
def product_list(request):
    products=Product.objects.all()
    return render(request, "product_list.html",{"products":products})
#products creat
def product_create(request):
    if request.method == "POST":
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect ("product_list")
    else:
        form=ProductForm()
            
    return render(request, "product_form.html",{"form":form})    
    
#product update 
def product_update(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm(instance=product)

    return render(request, "product_form.html", {"form": form})

#delte
def product_delete(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        product.delete()
        return redirect("product_list")

    return render(request, "product_delete.html", {"product": product})