import stripe
from django.core.handlers.wsgi import WSGIRequest
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from config import STRIPE_API_KEY
from stripe_api.models import Item, Order

stripe.api_key = STRIPE_API_KEY


def index(request):
    """Return cons text for / path"""
    return HttpResponse(
        "django server is running, check https://github.com/Neafiol/Django-Stripe-Api for more information")


def buy_router(request: WSGIRequest, item_id: int) -> JsonResponse:
    """
    Generate stripe session ID for purchase

    :param request:
    :param item_id: id if item for purchase in database
    :return: dict with session_id from stripe
    """

    item = Item.objects.get(id=item_id)
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': item.get_currency_display(),
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': item.price * 100,  # stripe calc cents in price value
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='https://neafiol.github.io',
            cancel_url='https://neafiol.github.io',
        )
    except stripe.error.InvalidRequestError as e:
        # for example too low sum
        return HttpResponse(str(e))

    return JsonResponse({'session_id': session.id})


def order_new_router(request: WSGIRequest) -> JsonResponse:
    """
    Create new order object in database

    :param request:
    :return: dict with order_id
    """
    order = Order.objects.create()
    return JsonResponse({'order_id': order.id})


def order_buy_router(request: WSGIRequest, order_id: int) -> JsonResponse:
    """
    Generate stripe session ID for order's purchase

    :param request:
    :param order_id: id of order in database
    :return: dict with session_id from stripe
    """

    order = Order.objects.get(id=order_id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': "Корзина толваров",
                },
                'unit_amount': order.total,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='https://neafiol.github.io',
        cancel_url='https://neafiol.github.io',
    )
    return JsonResponse({'session_id': session.id})


def order_put_router(request, order_id):
    """
    Put new item in order,
    request.GET need contain `item_id` field

    :param request:
    :param order_id: id of order in database
    :return: the object in the form of a dict
    """

    item = Item.objects.get(id=request.GET.get('item_id'))
    order = Order.objects.get(id=order_id)
    order.items.append(item.id)
    order.total += item.price
    order.save()
    return JsonResponse(model_to_dict(order))


def item_router(request, item_id):
    """
    Return web page with information about item

    :param request:
    :param item_id:
    :return:
    """
    item = Item.objects.get(id=item_id)
    return render(request, "stripe_api/order.html", context=model_to_dict(item))
