from django.urls import include, path
from rest_framework import routers
from TastyRecipes_application import views


urlpatterns = [
    # path('', views.user_list),
    path('', views.all_recipes),
    path('<int:recipe_id>/', views.recipe),
    path('<int:recipe_id>/comment/', views.comment_list),
    path('comment/', views.comment_new),
    path('comment/<int:pk>/', views.comment_update),
    path('<int:recipe_id>/ingredients/', views.Ingredient_list),
    path('ingredients/', views.Ingredients_new),
    path('<int:category_id>/recipe/', views.recipe_list),
    path('category/recipe/', views.recipe_new),
    path('category/recipe/<int:pk>/', views.recipe_update),
    path('categories/', views.category_list),
    path('favourites/list/', views.favourite),
    path('<int:recipe_pk>/favourites/create/', views.favourite_create),
    path('<int:fav_pk>/favourite/delete/', views.favorite_update),
    path('recipe/comment/<int:comment_pk>/', views.comment),
    path('substances/', views.substance_list),
    path('ingredient/<int:ingredient_pk>/', views.ingredient),
]