from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import MenuItem


def hello(request):
    return HttpResponse("Hello World")


def menu_item(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    return HttpResponse(f"{item.name}: {item.description}.")


def menu_card(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    return render(request, "little_lemon/menu_card.html", {"item": item})
