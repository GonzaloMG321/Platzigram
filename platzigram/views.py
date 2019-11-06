"""Platzigram views"""
from django.http import HttpResponse
from datetime import datetime
import json
def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs ')
    return HttpResponse('Hi, current server time: {} '.format(
        now
    ))

def sorted_integers(request):
    """Return a JSON response"""    
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_integers = sorted(numbers)
    # import pdb; pdb.set_trace()
    data = {
        'status': 'ok',
        'numbers': sorted_integers,
        'message': 'Everything is correct'
    }
    return HttpResponse(
        json.dumps(data, indent=4), 
        content_type='application/json'
    )

def say_hi(request, name, age):
    message = ''
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello {}, Welcome to platzigram'.format(name)

    return HttpResponse(message)