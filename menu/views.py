# from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Food, Beverage
from django.db.models import Q


def index(request):
        query = request.GET.get("q")
        food_items = Food.objects.all()
        beverage_items = Beverage.objects.all()
        template = loader.get_template('menu/index.html')
        if query:
            food_items = food_items.filter(
                Q(item_name__icontains=query)
            ).distinct()
            beverage_items = beverage_items.filter(
                Q(item_name__icontains=query)
            ).distinct()
        context = {'food_items': food_items}
        context.update({'beverage_items': beverage_items})

        return HttpResponse(template.render(context, request))


def detail_food(request, food_id):
    try:
        food = Food.objects.get(pk=food_id)
    except Food.DoesNotExist:
        raise Http404('Food does not exist')
    return render(request, 'menu/detail.html', {'food': food})


def detail_beverage(request, beverage_id):
    try:
        beverage = Beverage.objects.get(pk=beverage_id)
    except Beverage.DoesNotExist:
        raise Http404('Beverage does not exist')
    return render(request, 'menu/detail.html', {'beverage': beverage})