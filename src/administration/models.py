from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField, Model, DateTimeField, BooleanField, ImageField, URLField, SlugField, CharField, SET_NULL
from django.utils.translation import gettext_lazy as _
from django.db import models


class User(AbstractUser):
    email = EmailField(_('email address'), unique=True)

    class Meta:
        db_table = 'auth_user'


class PublishableModel(models.Model):
    is_published = models.BooleanField()

    class Meta:
        abstract = True


class CreatedUpdatedModel(models.Model):
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ExampleModel(Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    date = models.DateField(null=True)
    age = models.IntegerField()


class Partner(PublishableModel, CreatedUpdatedModel):
    name = CharField(max_length=100)
    slug = SlugField()
    website = URLField(blank=True, default=None)
    logo = ImageField(blank=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'partners'

class Faq(PublishableModel, CreatedUpdatedModel):
    question = models.CharField(max_length=300)
    answer = models.TextField(max_length=1000)

    def __str__(self):
        return self.question

    class Meta:
        db_table = 'faqs'

class Organisation(PublishableModel, CreatedUpdatedModel):
    name = models.CharField(max_length=20)
    slug = models.SlugField(blank=True)
    website = models.URLField(blank=True, default=None)
    description = models.TextField(max_length=300, blank=True)
    location = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'organisations'

class Opportunity(CreatedUpdatedModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    url = models.URLField(blank=True, default=None)
    description = models.TextField(max_length=300)
    deadline = models.DateTimeField()
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "opportunity"
        verbose_name_plural = "opportunities"
        db_table = 'opportunities'


class MenuItem(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField()
    link = models.URLField()
    image = models.ImageField(blank=True, default=None)
    parent = models.CharField(max_length=30, blank=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'menu_items'

class Article(PublishableModel, CreatedUpdatedModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    image = models.ImageField(blank=True, default=None)
    description = models.CharField(max_length=2000)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'articles'

class Newsletter(PublishableModel, CreatedUpdatedModel):
    email = models.CharField(max_length=50)
    opportunity_categories = models.ManyToManyField(OpportunityCategory)
    other = models.CharField(max_length=500)

    class Meta:
        db_table = 'newsletters'

    def __str__(self):
        return self.email


class WantToHelp(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField(max_length=255)
    description = models.TextField()

    class Meta:
        db_table = 'want_to_help'

class OpportunityCategory(CreatedUpdatedModel):
    name = models.CharField(max_length=225)
    slug = models.SlugField()
    opportunities = models.ManyToManyField(Opportunity)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(Organisation, on_delete=SET_NULL, null=True)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.user

    class Meta:
        db_table = 'user_profiles'
