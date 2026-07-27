from django.db import migrations


MENU_ITEMS = [
    {
        "name": "Bruschetta",
        "price": 8,
        "menu_item_description": "Grilled bread rubbed with garlic and topped with diced tomatoes, fresh basil and olive oil.",
    },
    {
        "name": "Greek salad",
        "price": 10,
        "menu_item_description": "Tomatoes, cucumbers, olives and feta cheese tossed in a lemon-oregano vinaigrette.",
    },
    {
        "name": "Grilled fish",
        "price": 18,
        "menu_item_description": "Catch of the day, grilled and served with a lemon-herb sauce and seasonal vegetables.",
    },
    {
        "name": "Lemon dessert",
        "price": 7,
        "menu_item_description": "Layered lemon cake with a light mascarpone cream, the restaurant's signature dessert.",
    },
]


def seed_menu_items(apps, schema_editor):
    Menu = apps.get_model('restaurant', 'Menu')
    for item in MENU_ITEMS:
        Menu.objects.get_or_create(name=item["name"], defaults=item)


def remove_menu_items(apps, schema_editor):
    Menu = apps.get_model('restaurant', 'Menu')
    Menu.objects.filter(name__in=[item["name"] for item in MENU_ITEMS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_remove_booking_comment_remove_booking_guest_number_and_more'),
    ]

    operations = [
        migrations.RunPython(seed_menu_items, remove_menu_items),
    ]
