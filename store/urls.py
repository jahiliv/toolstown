from django.urls import path
from .views import signin, signup, signout, Index,Cart,checkout, customerorder, about
# from store import views
from .middlewares.auth import auth_middleware

urlpatterns = [
   # path('', index, name="index"),
   path('',Index.as_view(), name="index"),
   path('signup/',signup, name="signup"),
   path('signin/',signin, name="signin"),
   path('signout/',signout, name="signout"),
   path('cart/',auth_middleware(Cart.as_view()), name="cart"),
   path('order/',auth_middleware(customerorder), name="order"),
   path('about/',about, name="about"),
   path('checkout', auth_middleware(checkout), name="checkout"),

]
