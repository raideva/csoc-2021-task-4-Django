# Generated by Django 2.2.1 on 2021-07-15 06:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210714_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcopy',
            name='borrow_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
