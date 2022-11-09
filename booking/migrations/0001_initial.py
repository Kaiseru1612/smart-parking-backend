# Generated by Django 4.1.3 on 2022-11-09 09:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("parking_lot", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("booking_duration", models.FloatField(default=10)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("BOOKED", "Booked"),
                            ("PARKING", "Parking"),
                            ("FINSHED", "Finished"),
                            ("CANCEL", "Cancel"),
                        ],
                        default="BOOKED",
                        max_length=10,
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                (
                    "parking_lot",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="parking_lot",
                        to="parking_lot.parkinglot",
                    ),
                ),
            ],
        ),
    ]
