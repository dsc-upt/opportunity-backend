# Generated by Django 3.1.4 on 2020-12-20 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('is_published', models.BooleanField()),
                ('slug', models.SlugField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, default=None, upload_to='')),
                ('description', models.CharField(max_length=2000)),
            ],
            options={
                'db_table': 'articles',
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('question', models.CharField(max_length=300)),
                ('answer', models.TextField(max_length=1000)),
            ],
            options={
                'db_table': 'faqs',
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('link', models.URLField()),
                ('image', models.ImageField(blank=True, default=None, upload_to='')),
                ('parent', models.CharField(blank=True, default=None, max_length=30)),
            ],
            options={
                'db_table': 'menu_items',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('is_published', models.BooleanField()),
                ('slug', models.SlugField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('website', models.URLField(blank=True, default=None)),
                ('logo', models.ImageField(blank=True, default=None, upload_to='')),
            ],
            options={
                'db_table': 'partners',
            },
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=50)),
                ('other', models.CharField(max_length=500)),
                ('opportunity_categories', models.ManyToManyField(to='administration.OpportunityCategory')),
            ],
            options={
                'db_table': 'newsletters',
            },
        ),
    ]
