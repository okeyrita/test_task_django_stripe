from django.shortcuts import render
from .models import Item
from django.http import JsonResponse
import stripe


KEY_PATH = '../test_task/data/stripe_key.txt'
with open(KEY_PATH, 'r') as stripe_file:
    keys = stripe_file.read().splitlines()
    stripe.api_key = keys[0]
    public_api_key = keys[1]


def start_page(request):
    '''
    Show list of all items. 
    '''
    items = Item.objects.all()

    return render(request, 'pay_system/start_page.html',
                  {'title': 'List of all Items', 'items': items})


def item_page(request, pk):
    '''
    Show page with current item.
    '''
    item = Item.objects.get(id=pk)

    return render(request, 'pay_system/index.html',
                  {'item': item,
                   'stripe_key': stripe.api_key,
                   'public_sk': public_api_key})


def create_session(item):
    '''
    Create stripe session.
    '''
    session = stripe.checkout.Session.create(
        success_url='http://127.0.0.1:8000/',
        cancel_url='http://127.0.0.1:8000/',
        payment_method_types=["card"],
        line_items=[
            {
                    "name": item.name,
                    "quantity": int(item.price)*100,
                    "currency": 'rub',
                    "amount": 1
            },
        ],
        mode="payment",
    )

    return session


def buy_item(request, pk):
    '''
    Get stripe session_id.
    '''
    item = Item.objects.get(id=pk)
    session = create_session(item=item)

    return JsonResponse({'session_id': session.id})
