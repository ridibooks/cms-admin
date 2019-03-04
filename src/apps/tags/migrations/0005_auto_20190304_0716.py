# Generated by Django 2.1.2 on 2019-03-04 07:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tags', '0004_auto_20190304_0652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='creator_id',
        ),
        migrations.AddField(
            model_name='tag',
            name='creator',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.PROTECT, related_name='tags_logs', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
