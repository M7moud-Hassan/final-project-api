# Generated by Django 4.1.7 on 2023-03-17 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_registeruser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerfreelancer',
            name='user_image',
            field=models.ImageField(null=True, upload_to='images/freelancer/profile/'),
        ),
    ]