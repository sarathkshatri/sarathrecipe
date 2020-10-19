from rest_framework import serializers
from .models import Recipe, Ingredients, Favorite, Comment, Category, Substance

from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('pk', 'user', 'recipe', 'username', 'recipe_name', 'comment',)


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ('pk', 'recipe', 'substance', 'amount', 'unit', 'substance_name')


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('pk', 'user', 'username', 'category', 'category_name', 'recipe_name', 'instructions')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('pk', 'category_name')


class FavoirteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('pk', 'user', 'recipe', 'username', 'recipe_name',)


class SubstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Substance
        fields = ('pk', 'substance_name')
