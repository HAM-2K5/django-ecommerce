from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from cart.cart import Cart
from django.shortcuts import get_object_or_404


@login_required
def checkout(request):
    cart = Cart(request)

    if request.method == 'POST':
        full_name = request.POST['full_name']
        address = request.POST['address']
        phone = request.POST['phone']

        order = Order.objects.create(
            user=request.user,
            full_name=full_name,
            address=address,
            phone=phone
        )

        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
            )

        cart.clear()
        return redirect('dummy_payment', order_id=order.id)

    return render(request, 'orders/checkout.html')

def order_success(request):
    return render(request, 'orders/order_success.html')

def dummy_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    # simulate successful payment
    order.paid = True
    order.save()

    return redirect('order_success')

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/my_orders.html', {'orders': orders})
