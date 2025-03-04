# Generated by Django 2.2.1 on 2021-07-14 06:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20190607_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='number',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bookcopy',
            name='borrow_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bookcopy',
            name='borrower',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='borrower', to=settings.AUTH_USER_MODEL),
        ),
    ]
