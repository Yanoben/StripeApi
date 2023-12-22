from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
import stripe

from django.conf import settings
from StripeApi.models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY
public_key = settings.STRIPE_PUBLISHABLE_KEY


def get_stripe_session_id(request, id):

    item = get_object_or_404(Item, id=id)

    session = stripe.checkout.Session.create(
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {"name": item.name},
                    "unit_amount": item.price,
                },
                "quantity": 1,
            },
        ],
        mode="payment",
        success_url=settings.DOMAIN + '/success/',
        cancel_url=settings.DOMAIN + '/cancel/'
    )


    return JsonResponse({'sessionId': session.id})


def get_info_about_item(request, id):
    '''Выдаёт данные продукта + кнопку для оплаты'''
    item = get_object_or_404(Item, id=id)
    return render(request, 'stripe/checkout.html', {'item': item, 'public_key': public_key})


def success(request):
    return HttpResponse('Успешно')


def cancel(request):
    return HttpResponse("No, that's wrong!")


def all_obj(request):
    items = Item.objects.all()

    return render(request, 'stripe/items.html', {'items': items})