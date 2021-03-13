from django.shortcuts import render, redirect
from .models import Order, Product
from django.db.models import Avg, Max, Min, Sum

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])

    # grabs the product id (value in form) to query product based up it's id
    product_id = request.POST["product_id"]
    item_selected = Product.objects.get(id=product_id)
    price_from_form = float(item_selected.price)

    total_charge = quantity_from_form * price_from_form
    request.session['total'] = total_charge

    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    print("Charging credit card...")
    print(f"Adding ${request.session['total']} to total")
    return redirect('/completed')

def checkout_complete(request):
    context = {
    "all_orders": Order.objects.all(),
    "recent_order_total": request.session['total'],
    "total_history": Order.objects.all().aggregate(Sum('total_price')),
    "quantity_history": Order.objects.all().aggregate(Sum('quantity_ordered')),
    }
    return render(request, "store/checkout.html", context)
