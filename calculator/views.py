from django.shortcuts import render
from django.urls import reverse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'krabsburger': {
        'булочка, шт': 1,
        'соус, гр': 10,
        'котлета, шт': 1,
        'пикули, шт': 2,
        'лук, ломтик': 1,
        'помидор, ломтик': 1,
        'салат, лист': 1,
    },
    # можете добавить свои рецепты ;)
}


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def home_view(request):
    template_name = 'calculator/homepage.html'
    pages = {
        'omlet': reverse('omlet'),
        'pasta': reverse('pasta'),
        'buter': reverse('buter'),
        'krabsburger': reverse('krabsburger'),
    }
    context = {'pages': pages}
    return render(request, template_name, context)


def calc(request, meal):
    template_name = 'calculator/index.html'
    servings = int(request.GET.get('servings', 1))
    recipe = {ingredient: round(quantity * servings, 2) for ingredient, quantity in DATA[meal].items()}
    context = {
        'recipe': recipe,
        'person': range(1, 10),
        'meal': meal
    }
    return render(request, template_name, context)