# Generated by Django 2.1.2 on 2019-03-04 06:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_auto_20190227_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tag',
            name='is_use',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='tag',
            name='reg_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]