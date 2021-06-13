from django.shortcuts import render,redirect
from .models import products,order
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    product_objects = products.objects.all()
    #search code
    item_name = request.GET.get('item_name')
    if item_name!= '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)
    #paginator code
    paginator = Paginator(product_objects,4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)
    return render(request,'index.html',{'product_objects':product_objects})

def detail(request,id):
    product_object = products.objects.get(id=id)
    return render(request,'detail.html',{'product_object':product_object})

def checkout(request):

    if request.method == "POST":
        items = request.POST.get('items',"")
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        state = request.POST.get('state',"")
        zipcode = request.POST.get('zipcode',"")
        total = request.POST.get('total',"")
        order1 = order(items=items,name=name,email=email,address=address,city=city,state=state,zipcode=zipcode,total=total) 
        order1.save()  
    return render(request,'checkout.html')
def register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}, your account has been created' )
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request,'user.html',{'form':form})
@login_required
def Profilepage(request):
    return render(request,'profile.html')
