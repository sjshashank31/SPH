from django.core import serializers
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .forms import PaymentForm, Crop
from .models import Product, Payment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import authenticate, login


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
    return render(request, 'home.html')


@login_required(login_url='/login/')
def add_payment(request):
    products = Product.objects.all()
    crops = Crop.objects.all()
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            bill_no = form.cleaned_data['bill_no']
            user = request.user
            crop = form.cleaned_data['crop']
            product = form.cleaned_data['product']
            qty_used = form.cleaned_data['qty_used']
            used_for = form.cleaned_data['used_for']
            payment_date = form.cleaned_data['payment_date']
            male_labour_used = form.cleaned_data['male_labour_used']
            female_labour_used = form.cleaned_data['female_labour_used']
            labour_amount = form.cleaned_data['labour_amount']
            petrol_amount = form.cleaned_data['petrol_amount']
            diesel_amount = form.cleaned_data['diesel_amount']
            total_amount = form.cleaned_data['total_amount']
            remarks = form.cleaned_data['remarks']

            Payment.objects.create(bill_no=bill_no,
                                   user=user,
                                   crop=crop,
                                   product=product,
                                   qty_used=qty_used,
                                   used_for=used_for,
                                   payment_date=payment_date,
                                   male_labour_used=male_labour_used,
                                   female_labour_used=female_labour_used,
                                   labour_amount=labour_amount,
                                   petrol_amount=petrol_amount,
                                   diesel_amount=diesel_amount,
                                   total_amount=total_amount,
                                   remarks=remarks)

            if product:
                product = Product.objects.get(code=product)
                product.volume = product.volume-qty_used
                product.save()
            return redirect("farm:payments")
        else:
            print(form.errors)
            return render(request, 'add_payment.html', {'form': form, 'products': products, 'crops':crops})

    form = PaymentForm()

    return render(request, 'add_payment.html', {'form': form, 'products': products, 'crops': crops})


@login_required(login_url='/login/')
def get_payments(request):
    payments = Payment.objects.all()
    products = Product.objects.all()
    crops = Crop.objects.all()

    return render(request, 'payments.html', {'payments': payments, 'products': products, 'crops': crops})


@login_required(login_url='/login/')
def filter_crop(request, crop):
    crops = Crop.objects.all()
    payments = Payment.objects.filter(crop=crop).all()
    return render(request, 'payments.html', {'payments': payments, 'crops': crops})


@login_required(login_url='/login/')
def update_payment(request, bill_no):
    crops = Crop.objects.all()
    products = Product.objects.all()
    payment = get_object_or_404(Payment, bill_no=bill_no)
    form = PaymentForm(instance=payment)
    print(form)
    return render(request, 'update_payment.html', {'form': form, 'products': products, 'crops':crops})


@login_required(login_url='/login/')
def get_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products':products})

@login_required(login_url='/login/')
def get_product_details(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_details.html', {'product':product})