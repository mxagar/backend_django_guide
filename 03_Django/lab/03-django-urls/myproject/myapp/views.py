from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1> Welcome to Little Lemon! </h1>")


def drinks(request, drink_name):
    drink = {
        "mocha": "type of coffee",
        "tea": "type of beverage",
        "lemonade": "type of refreshment",
        "espresso": "type of strong coffee",
    }
    choice_of_drink = drink.get(drink_name, "drink not found")
    return HttpResponse(f"<h2> {drink_name} </h2>" + choice_of_drink)
