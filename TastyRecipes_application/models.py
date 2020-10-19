from datetime import timezone

from django.contrib.postgres.fields import ArrayField
from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.category_name)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    recipe_name = models.CharField(max_length=50, blank=False, null=False)
    instructions = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default='')

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.recipe_name)

    def username(self):
        return self.user.username

    def category_name(self):
        return self.category.category_name

    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,default='')

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def username(self):
        return self.user.username

    def recipe_name(self):
        return self.recipe.recipe_name

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'Favorite'
        verbose_name_plural = 'Favorite'

    def __str__(self):
        return "{}'s {}".format(self.user,self.recipe)


class Substance(models.Model):
    substance_name = models.CharField(max_length=15)

    def __str__(self):
        return str(self.substance_name)

    class Meta:
        verbose_name = 'Substance'
        verbose_name_plural = 'Substance'


class Ingredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,default='')
    substance = models.ForeignKey(Substance, on_delete=models.CASCADE,default='')
    amount = models.IntegerField()
    unit = models.CharField(max_length=50)

    def __str__(self):
        return "{}'s {}".format(self.recipe,self.unit)

    def recipe_name(self):
        return self.recipe.recipe_name

    def substance_name(self):
        return self.substance.substance_name

    class Meta:
        verbose_name = 'Ingredients'
        verbose_name_plural = 'Ingredients'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, default='')
    comment = models.TextField()

    def __str__(self):
        return "{}'s {}".format(self.user, self.comment)

    def recipe_name(self):
        return self.recipe.recipe_name

    def username(self):
        return self.user.username

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'