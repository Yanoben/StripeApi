from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
import stripe
from .models import Item

stripe.api_key = "sk_test_YOUR_STRIPE_SECRET_KEY"


def home(request):
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})


def get_item(request, id):
    item = get_object_or_404(Item, pk=id)
    return render(request, 'item.html', {'item': item})


def buy_item(request, id):
    item = get_object_or_404(Item, pk=id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': int(item.price * 100),  # в центах
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('success')),
        cancel_url=request.build_absolute_uri(reverse('cancel')),
    )
    return JsonResponse({'session_id': session.id})
