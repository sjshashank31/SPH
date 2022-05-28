from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import authenticate, login


def expenses(request, id):
    crop = Crop.objects.get(id=id)
    tasks = Task.objects.filter(crop=crop).all()
    return render(request, 'expense_details.html')


def login_view(request):
    if request.user.is_authenticated:
        messages.success(request, "you are already logged in")
        return redirect("farm:home")
    else:
        if request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("farm:home")
            else:
                messages.error(request, "user and password does not match")
                return render(request, 'registration/login.html')
        else:
            return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "you are successfully logged out")
    return redirect('farm:home')


@login_required(login_url='/login/')
def home(request):
    crops = Crop.objects.all()
    return render(request, 'home.html', {'crops':crops})


@login_required(login_url='/login/')
def add_crop(request):
    if request.method == "POST":
        form = CropForm(request.POST)
        if form.is_valid():
            crop_name = form.cleaned_data['crop_name']
            crop_area = form.cleaned_data['crop_area']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            crop = Crop.objects.create(user=request.user, crop_name=crop_name, crop_area=crop_area, start_date=start_date, end_date=end_date)
            crop.slug_save()
            messages.success(request, "Crop Added successfully")
            return redirect("farm:crops")
        else:
            form = CropForm(request.POST)
            return render(request, 'add_crop.html', {'form': form})

    form = CropForm()
    return render(request, 'add_crop.html', {'form':form})


@login_required(login_url='/login/')
def add_product_category(request):

    if request.POST:
        form = ProductCategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("farm:product_categories")
    form = ProductCategoryForm()
    return render(request, 'product_category_form.html', {"form":form})


@login_required(login_url='/login/')
def product_categories(request):
    categories = ProductCategory.objects.all()
    return render(request, 'product_categories.html', {"categories": categories})


@login_required(login_url='/login/')
def get_crops(request):
    crops = Crop.objects.all()
    return render(request, 'crops.html', {'crops': crops})


@login_required(login_url='/login/')
def add_product(request):
    product_categories = ProductCategory.objects.all()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product_code = form.cleaned_data['product_code']
            product_name = form.cleaned_data['product_name']
            product_description = form.cleaned_data['product_description']
            product_type = form.cleaned_data['product_type']
            product_category = form.cleaned_data['product_category']
            volume = form.cleaned_data['volume']
            price = form.cleaned_data['price']
            product = Product.objects.create(user=request.user,
                                             product_code=product_code,
                                             product_name=product_name,
                                             product_description=product_description,
                                             product_type=product_type,
                                             product_category=product_category,
                                             volume=volume,
                                             price=price
                                             )
            product.add_product()
            messages.success(request, "Product Added successfully")
            return redirect("farm:products")
        else:
            form = ProductForm(request.POST)
            return render(request, 'add_product.html', {'form': form, 'product_categories': product_categories})

    form = ProductForm()
    print(form)
    return render(request, 'add_product.html', {'form': form, 'product_categories': product_categories})


@login_required(login_url='/login/')
def get_products(request):
    products = Product.objects.all().order_by('-created_at')

    paginator = Paginator(products, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'products.html', {'page_obj': page_obj})


@login_required(login_url='/login/')
def get_product_details(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_details.html', {'product':product})


@login_required(login_url='/login/')
def add_task(request):
    crops = Crop.objects.all()
    if request.POST:
        form = TaskForm(request.POST)
        if form.is_valid():
            crop = form.cleaned_data['crop']
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            task = Task.objects.create(user= request.user, crop=crop, title=title, description=description)
            task.save()
            return redirect('farm:task_list')
        return HttpResponse("Please Go back and fill correct information")
    form = TaskForm()
    return render(request, 'add_task.html', {'form': form, 'crops': crops})


def get_tasks_list(request):
    tasks = Task.objects.all()
    paginator = Paginator(tasks, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'tasks.html', {'page_obj': page_obj})


def update_task(request, id):
    task = get_object_or_404(Task, id=id)
    form = TaskForm(request.POST or None, instance=task)

    if form.is_valid():
        form.save()
        return redirect('farm:task-list')
    # return HttpResponse("Please Go back and fill correct information")

    return render(request, 'update_task.html', {'form': form})


def used_product(request):
    tasks = Task.objects.all()
    products = Product.objects.all()
    if request.POST:
        form = OutwardProductForm(request.POST)
        if form.is_valid():
            user = request.user
            task = form.cleaned_data['task']
            code = form.cleaned_data['code']
            volume_outwarded = form.cleaned_data['volume_outwarded']
            used_for = form.cleaned_data['used_for']
            product = Product.objects.get(product_code=code)
            price = (product.volume/product.price)*volume_outwarded
            outward_product = OutwardProduct(user=user, task=task, code=code, volume_outwarded=volume_outwarded, used_for=used_for, price=price)
            outward_product.update_stock()
            return redirect('farm:used_products')
        return HttpResponse(form)
    form = OutwardProductForm()
    return render(request, 'outward_product_form.html', {'form': form, 'products': products, 'tasks': tasks})


def get_used_products(request):
    products = OutwardProduct.objects.all().order_by('-used_date')
    paginator = Paginator(products, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'used_products_list.html', {'page_obj': page_obj})


def get_inward_products(request):
    products = InwardProduct.objects.all()
    return render(request, 'inward_products.html', {'products':products})


def add_labour(request):
    tasks = Task.objects.all()
    if request.POST:
        form = LabourForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            male_count = form.cleaned_data['male_count']
            female_count = form.cleaned_data['female_count']
            labour = Labour(user=request.user, task=task, male_count=male_count, female_count=female_count)
            labour.save_data()
            return redirect("farm:labour_payments")
        form = LabourForm(request.POST)
        return render(request, 'labour_form.html', {'form': form, 'tasks': tasks})
    form = LabourForm()

    return render(request, 'labour_form.html', {'form': form, 'tasks': tasks})


def labour_details(request):
    labours = Labour.objects.all().order_by('-date')
    paginator = Paginator(labours, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'labour_payments.html', {'page_obj': page_obj})