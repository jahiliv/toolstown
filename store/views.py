from django.db import reset_queries
from django.shortcuts import redirect, render
from django.http import request
from .models.product import Product
from .models.category import Category
from .models.extendeduser import ExtendedUser
from django.contrib.auth.models import User
from django.contrib import auth
from django.views import View
from .models.order import Order
from django.contrib import messages
# from store.middlewares.auth import auth_middleware

# Create your views here.
class Index(View):

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]=quantity-1
                else : 
                     cart[product]=quantity+1
            else:
                cart[product] = 1
        else:
            cart= {}
            cart[product]= 1

        request.session['cart'] = cart
        # print('cart',request.session['cart'])
        # print(product)
        return redirect('index')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}

        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_products_by_categoryID(categoryID)
        else : 
            products = Product.get_all_products()

        data = {}
        data['products']=products
        data['categories']=categories
        # print('your email is : ',request.session.get('user_email'))

        return render (request, 'index.html',data)
        # return HttpResponse("hello")

def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['confrimpassword']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error': "User Name already exists"})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST
                ['username'], password=request.POST['password'],first_name=request.POST['firstname'],
                last_name=request.POST['lastname'], email=request.POST['email'])
                phnum = request.POST['phone']
                age = request.POST['age']
                nid = request.POST['nid']
                address = request.POST['address']
                profession = request.POST['profession']
                newuser = ExtendedUser(nid=nid,age=age, 
                phone_no=phnum, address=address,profession=profession, user=user)
                newuser.save()
                
                return redirect(signin)
        else:
            return render(request, 'signup.html', {'error': "Password Doesn't Match"})
    else : 
        return render (request, 'signup.html')

def signout(request):
    # auth.logout(request)
    request.session.clear()
    return redirect('index')
    # return redirect(Index)

def signin(request):
    if request.method == "POST":
        
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            request.session['user_id'] = user.id
            request.session['user_email'] = user.email
            
            # return redirect(Index)
            return redirect('index')
        else:
           return render(request, 'signin.html', {"error": "Invaild Login Credentials"}) 

    else:
        return render (request, 'signin.html')

def customerorder(request):
    user = request.session.get('user_id')
    data = {}
    orders_pending= Order.get_orders_by_customer_pending(user)
    orders_delivered= Order.get_orders_by_customer_delivered(user)
    orders_completed = Order.get_orders_by_customer_compeleted(user) 

    data['orders_pending'] = orders_pending
    data['orders_delivered'] = orders_delivered
    data['orders_completed'] = orders_completed

   
    return render(request, 'order.html', data)
    

def about(request):
    return render (request, 'about.html')

class Cart(View):
    def get(self, request):
        productID = None
        productID = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(productID)
        # print(products)
        return render(request, 'cart.html', {'products': products})

def checkout(request):
    if request.method=="POST":
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        user = request.session.get('user_id')
        # print(address, phone, user)
        cart = request.session.get('cart')
        prodcuts =Product.get_products_by_id(list(cart.keys()))
        for product in prodcuts:
            productorder = Order(user=User(id = user),product = product, baseprice = product.base_price,borrowprice=product.borrow_price, address = address, phone = phone,quantity = cart.get(str(product.id)))
            productorder.save()

            request.session['cart']= {}
            messages.success(request, 'Your product has ordered, we will contact with you within 2-4 days')
        return redirect('order')
            # return render(request, 'cart.html')