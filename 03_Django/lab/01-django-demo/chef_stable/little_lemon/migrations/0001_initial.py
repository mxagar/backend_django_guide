# Generated for the MVT example in this repository.

from django.db import migrations, models


def seed_menu_items(apps, schema_editor):
    MenuItem = apps.get_model("little_lemon", "MenuItem")
    MenuItem.objects.get_or_create(
        id=1,
        defaults={
            "name": "Pasta",
            "description": "Type of Italian cuisine",
        },
    )
    MenuItem.objects.get_or_create(
        id=2,
        defaults={
            "name": "Falafel",
            "description": "Type of Middle Eastern cuisine",
        },
    )


def remove_seed_menu_items(apps, schema_editor):
    MenuItem = apps.get_model("little_lemon", "MenuItem")
    MenuItem.objects.filter(id__in=[1, 2]).delete()


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MenuItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=255)),
            ],
        ),
        migrations.RunPython(seed_menu_items, remove_seed_menu_items),
    ]
