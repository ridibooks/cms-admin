# Generated by Django 2.1.2 on 2019-03-04 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0003_auto_20190304_0626'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='creator',
            new_name='creator_id',
        ),
        migrations.AlterField(
            model_name='tag',
            name='is_use',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tag',
            name='reg_date',
            field=models.DateTimeField(),
        ),
    ]