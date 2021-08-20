from django.shortcuts import redirect, render
from django.urls import reverse

from store.models import Product
from .models import Cart,CartItem, Cupon
from .utils import get_cart, get_current_utc



def add_cart_item(request,cartitem_id):
    try:
        cartitem = CartItem.objects.get(id=cartitem_id)
        cartitem.quantity += 1    
    except CartItem.DoesNotExist:
        pass
    cartitem.save()
   
    return redirect(reverse("cart"))


def subtract_cart_item(request,product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return redirect(reverse("home-page"))

    cart = get_cart(request)
    try:
        cartitem = CartItem.objects.get(cart=cart, product=product)
        if cartitem.quantity > 1:
            cartitem.quantity -= 1    
            cartitem.save()
        else:
            cartitem.delete()
    except CartItem.DoesNotExist:
        pass

   
    return redirect(reverse("cart"))


def remove_cart_item(request, cartitem_id):
    try:
        cartitem = CartItem.objects.get(id = int(cartitem_id))
        cartitem.delete()
    except CartItem.DoesNotExist:
        pass

   
    return redirect(reverse("cart"))



def cart(request):
    context = {}
    cart = get_cart(request)
    cartitems = CartItem.objects.filter(cart=cart)

    if request.method == "POST":
        coupon_code = request.POST.get("coupon-code", None)
        if coupon_code:
            coupons = Cupon.objects.filter(code=coupon_code)
            if not coupons.exists():
                context["coupon_not_exists"] = "The coupon code doesn't exist."
            else:
                coupon = coupons.first()
                if get_current_utc() > coupon.expires_in:
                    context["coupon_not_exists"] = "The coupon code experid."
                else:
                    for cartitem in cartitems:
                        categories = []
                        for category in coupon.category.all():
                            categories.append(category.name)

                        category = cartitem.product.sub_category.name
                        if category in categories:
                            if cartitem.reduced_price:
                                cartitem.reduced_price = (cartitem.product.price * (100-coupon.stock))/100
                            else:
                                cartitem.reduced_price = (cartitem.product.price * (100-coupon.stock))/100
                            cartitem.save()


    context["cartitems"] = cartitems
    return render(request, "cart.html",context)


# def apply(request, code):
#     code = request.POST.get('code', None)
#     cupon = Cupon.objects.all()
#     if cupon.code == code and cupon.is_used==True:

