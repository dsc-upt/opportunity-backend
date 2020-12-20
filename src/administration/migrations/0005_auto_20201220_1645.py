# Generated by Django 3.1.4 on 2020-12-20 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0004_opportunitycategory_wanttohelp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunitycategory',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='opportunitycategory',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='is_published',
            field=models.BooleanField(),
        ),
    ]
