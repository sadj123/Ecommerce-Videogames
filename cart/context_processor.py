from django.contrib.auth.models import Group

def cart_total_amount(request):
    total = 0.0
    if Group.objects.get(name="Store") in request.user.groups.all():
        if request.session.get('cart'):
            for key, value in request.session['cart'].items():
                total = total + (float(value["price"]) * value["quantity"])
    return {'cart_total_amount':total}
