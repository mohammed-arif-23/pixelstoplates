# Import necessary modules
import base64
import string
import os
from django.shortcuts import render
from django.conf import settings
from .forms import ImageUploadForm
from PIL import Image
from .encoder import get_recipes
import json
current_dir = os.path.dirname(__file__)
def home_page(request):
    raw_image = None
    uploaded_image = None
    recipe_list_to_return = []
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            raw_image = form.cleaned_data['image']
            uploaded_image = base64.b64encode(
                raw_image.file.read()).decode('ascii')
            raw_image = Image.open(raw_image)
            recipe_list = get_recipes(raw_image)
            json_file_path = os.path.join(
                current_dir, 'static', 'main', 'indian_recipes.json')
            recipes_data = json.load(open(json_file_path))
            for i in range(len(recipe_list)):
                name = recipe_list[i]
                matching_recipes = list(
                    filter(lambda x: x["name"] == name, recipes_data))
                if len(matching_recipes) != 0:
                    print(len(matching_recipes))
                    matching_recipe = matching_recipes[0]
                    calories = matching_recipe['calories']
                    cooking_time = matching_recipe['cooking_time']
                    ingredients = matching_recipe['ingredients']
                    directions = matching_recipe['directions']
                    list_to_append = [string.capwords(
                        name), calories, cooking_time, ingredients, directions]
                    recipe_list_to_return.append(list_to_append)

    else:
        form = ImageUploadForm()
    return render(request, 'main/home.html', {'form': form, 'uploaded_image': uploaded_image,
                                                'recipe_list_to_return': recipe_list_to_return[:4],
                                                'similar_recipe_list': recipe_list_to_return[4:10]})
