# Generated by Django 3.0.8 on 2020-08-05 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor_general', '0013_auto_20200804_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(default='image-user.png', upload_to='profile_photos'),
        ),
    ]
