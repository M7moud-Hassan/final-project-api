# Generated by Django 4.1.7 on 2023-03-26 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0007_sendapply_is_hire'),
    ]

    operations = [
        migrations.AddField(
            model_name='hires',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
