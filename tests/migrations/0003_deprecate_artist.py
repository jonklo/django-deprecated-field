# Generated by Django 3.2.5 on 2021-07-10 23:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tests", "0002_deprecate_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="album",
            name="artist",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="albums",
                to="tests.artist",
            ),
        ),
    ]
