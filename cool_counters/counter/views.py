from django.shortcuts import render, get_object_or_404
from .models import Counter

def index(request):
    if len(Counter.objects.filter(key='counter')) == 0:
        counter = Counter(key='counter', value=0)
        counter.save()
    else:
        counter = get_object_or_404(Counter, key='counter')
    
    counter.value+=1
    counter.save()
    context = {'value': counter.value}
    return render(request, 'counter/index.html', context)

def submit(request):
    arg_firstname = request.GET.get('fname')
    arg_lastname = request.GET.get('lname')

    if len(Counter.objects.filter(key='counter')) == 0:
        counter = Counter(key='counter', value=0)
        counter.save()
    else:
        counter = get_object_or_404(Counter, key='counter')
    
    counter.value+=1
    counter.save()
    context = {
        'value': counter.value,
        'fname': arg_firstname,
        'lname': arg_lastname
            }

    response = render(request, 'counter/submit.html', context)
    return response


