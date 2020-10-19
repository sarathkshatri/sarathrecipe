from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import Category

from TastyRecipes_application.serializers import UserSerializer, CategorySerializer

from django.contrib.auth import get_user_model
User = get_user_model()
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Category,Recipe,Comment,Substance,Ingredients
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly



# @csrf_exempt
# @api_view(['GET'])
# def user_list(request):
#     permission_classes = IsAuthenticatedOrReadOnly
#     if request.method == 'GET':
#         users = User.objects.all()
#         serializer = UserSerializer(users, context={'request': request}, many=True)
#         return Response({'data': serializer.data})

@csrf_exempt
@api_view(['GET'])
def all_recipes(request):
    permission_classes = IsAuthenticatedOrReadOnly
    if request.method == 'GET':
        recipes = Recipe.objects.all()
        recipeSerializer = RecipeSerializer(recipes, context={'request': request}, many=True)
        return Response({'data': recipeSerializer.data})


@csrf_exempt
@api_view(['GET'])
def comment(request, comment_pk):
    permission_classes = IsAuthenticatedOrReadOnly
    if request.method == 'GET':
        comment = get_object_or_404(Comment, pk=comment_pk)
        serializer = CommentSerializer(comment, context={'request': request}, many=False)
        return Response({'data': serializer.data})



@csrf_exempt
@api_view(['GET'])
def comment_list(request, recipe_id):
    permission_classes = (IsAuthenticatedOrReadOnly)
    if request.method == 'GET':
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        comment = Comment.objects.filter(recipe_id=recipe_id)
        serializer = CommentSerializer(comment, context={'request': request}, many=True)
        return Response({'data': serializer.data})


@csrf_exempt
@api_view(['POST'])
def comment_new(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.data.get('username'))
        request.data['user'] = user.pk
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['PUT','DELETE'])
def comment_update(request, pk):
    permission_classes = (IsAuthenticatedOrReadOnly)
    try:
        comment = Comment.objects.get(pk=pk)
    except comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        if comment.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        user = User.objects.get(username=request.data.get('username'))
        request.data['user'] = user.pk
        serializer = CommentSerializer(comment, data = request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def ingredient(request, ingredient_pk):
    permission_classes = IsAuthenticatedOrReadOnly

    try:
        ingredient = Ingredients.objects.get(pk=ingredient_pk)
    except ingredient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        ingredient = get_object_or_404(Ingredients, pk=ingredient_pk)
        serializer = IngredientSerializer(ingredient, context={'request': request}, many=False)
        return Response({'data': serializer.data})
    if request.method == 'PUT':
        if ingredient.recipe.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = IngredientSerializer(ingredient, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        ingredient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET', 'POST'])
def Ingredient_list(request, recipe_id):
    permission_classes = (IsAuthenticatedOrReadOnly)

    if request.method == 'GET':
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        ingredients = Ingredients.objects.filter(recipe_id=recipe_id)
        serializer = IngredientSerializer(ingredients, context={'request': request}, many=True)
        return Response({'data': serializer.data})
    if request.method == 'POST':
        # recipe = get_object_or_404(Recipe, pk=recipe_id)
        serializer = IngredientSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
def Ingredients_new(request):
    if request.method == 'POST':
        serializer = IngredientSerializer(data=request.data)
        if serializer.recipe.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET'])
def recipe(request, recipe_id):
    permission_classes = IsAuthenticatedOrReadOnly
    if request.method == 'GET':
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        serializer = RecipeSerializer(recipe, context={'request': request}, many=False)
        return Response({'data': serializer.data})


@csrf_exempt
@api_view(['GET'])
def recipe_list(request,category_id):
    permission_classes = (IsAuthenticatedOrReadOnly)
    if request.method == 'GET':
        category = get_object_or_404(Category, pk=category_id)
        recipe = Recipe.objects.filter(category_id=category_id)
        serializer = RecipeSerializer(recipe, context={'request': request}, many=True)
        return Response({'data': serializer.data})


@csrf_exempt
@api_view(['GET'])
def substance_list(request):
    permission_classes = IsAuthenticatedOrReadOnly
    if request.method == 'GET':
        substances = Substance.objects.all()
        serializer = SubstanceSerializer(substances, context={'request': request}, many=True)
        return Response({'data': serializer.data})


@csrf_exempt
@api_view(['POST'])
def recipe_new(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.data.get('username'))
        request.data['user'] = user.pk
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['PUT', 'DELETE'])
def recipe_update(request, pk):
    permission_classes = IsAuthenticatedOrReadOnly

    try:
        recipe = Recipe.objects.get(pk=pk)
    except Recipe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        if recipe.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        user = User.objects.get(username=request.data.get('username'))
        request.data['user'] = user.pk
        serializer = RecipeSerializer(recipe, data=request.data, context={'request': request})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
@api_view(['GET', 'POST'])
def category_list(request):
    permission_classes = IsAuthenticatedOrReadOnly
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, context={ 'request': request }, many=True)
        return Response({'data': serializer.data})
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET'])
def favourite(request):
    permission_classes = IsAuthenticatedOrReadOnly
    if request.method == 'GET':

        favorite = Favorite.objects.filter(user = request.user)
        serializer = FavoirteSerializer(favorite, context={'request': request}, many=True)
        return Response({'data': serializer.data})

@csrf_exempt
@api_view(['POST'])
def favourite_create(request, recipe_pk):

    permission_classes = IsAuthenticatedOrReadOnly

    recipe1= get_object_or_404(Recipe, id = recipe_pk)


    if request.method == 'POST':
        favourites = Favorite.objects.filter(user=request.user, recipe_id=recipe_pk)
        for favor in favourites:
            if favor.recipe == recipe1:
                return Response({'message': "Already added in your favourites"})

        if Recipe.objects.filter(id=recipe_pk).exists():

                Favorite.objects.create(user=request.user, recipe=recipe1)
                return Response({'message': "Favourite Created succesfully"})
    return Response({'message': "Unable to create Favourite"})

@csrf_exempt
@api_view(['DELETE'])
def favorite_update(request, fav_pk):
    permission_classes = (IsAuthenticatedOrReadOnly)
    try:
        favorite = Favorite.objects.get(pk=fav_pk)
    except Favorite.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'DELETE':
        favorite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)