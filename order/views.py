from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.generic.list import ListView
from django.views.generic import DetailView
from .models import *
from gde.models import *
from cart.cart import Cart
import random

# Create your views here.

@login_required
def process_order(request):
    order = Order.objects.create(user = request.user, dispatcher= Dispatcher.randoms.all()[random.randint(0, len(Dispatcher.randoms.all()))])
    cart = Cart(request)
    order_lines = list()
    for key, value in cart.cart.items():
        order_lines.append(
            OrderLine(
                product=key,
                quantity=value["quantity"],
                order=order,
                price=value["price"]
            )
        )

    OrderLine.objects.bulk_create(order_lines)
    send_order_email(
        order =order,
        order_lines = order_lines,
        username = request.user.username,
        user_email = request.user.email,
        dispatcher= order.dispatcher,
    )

    cart.clear()
    messages.success(request, "Order create successfully")
    return redirect("list_videogame")

def send_order_email(**kwargs):
    subject = "Thank you for your order"
    html_message = render_to_string("Order.html", {
        "order": kwargs.get("order"),
        "order_lines": kwargs.get("order_lines"),
        "username": kwargs.get("username"),
        "dispatcher": kwargs.get("dispatcher")
    })
    plain_message = strip_tags(html_message)
    from_email = "game.designer.enterprise@gmail.com"
    to = kwargs.get("user_email")
    send_mail(subject, plain_message, from_email, [to], html_message=html_message)
