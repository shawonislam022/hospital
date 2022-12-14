# Generated by Django 4.1.2 on 2022-11-09 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("my_info", "0007_login"),
    ]

    operations = [
        migrations.CreateModel(
            name="Appointment",
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
                ("pname", models.CharField(max_length=50)),
                ("dept", models.CharField(max_length=50)),
                ("doctor", models.CharField(max_length=50)),
                ("phoneno", models.CharField(max_length=50)),
                ("problem", models.CharField(max_length=200)),
                ("email", models.CharField(max_length=50)),
                ("gender", models.CharField(max_length=50)),
            ],
        ),
    ]
