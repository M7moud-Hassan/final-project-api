# Generated by Django 4.1.7 on 2023-03-17 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0003_alter_imagesproject_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='certification',
            name='certification_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='profile_app.certificationtype'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imagesproject',
            name='image',
            field=models.ImageField(null=True, upload_to='images/Portflio_images/'),
        ),
    ]