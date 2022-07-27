from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Item, Purchase


def index(request):
    item_list = Item.objects.all()
    context = {'item_list': item_list}
    return render(request, 'list_item.html', context)


def detail_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    context = {'item': item}
    return render(request, 'detail_item.html', context)

#
# def result(request, question_id):
#     question = get_object_or_404(Question, id=question_id)
#     context = {'question': question}
#     return render(request, 'result.html', context)
#
#
# def vote(request, question_id):
#     question = get_object_or_404(Question, id=question_id)
#     choice = question.choice_set.get(id=request.POST['choice'])
#     choice.votes += 1
#     choice.save()
#     return HttpResponseRedirect(reverse('result', args=(question.id, )))
#
#
#
#
# def greetings(request):
#     return HttpResponse('Добро пожаловать в наш магазин')
#
