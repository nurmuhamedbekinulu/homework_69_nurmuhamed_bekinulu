from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
import json

# Create your views here.


def IndexView(request):
    return render(request, 'index.html')


def index(request):
    return render(request, 'webapp/index.html')


def post_data(request):
    try:
        data = json.loads(request.body)
        first_number = float(data['A'])
        second_number = float(data['B'])
        return first_number, second_number
    except:
        return False


@csrf_exempt
def add(request):
    if request.method == 'POST':
        if post_data(request) != False:
            first_number, second_number = post_data(request)
            answer = first_number + second_number
            return JsonResponse({'answer': answer})
    return JsonResponse({'error': 'Invalid Request'})


@csrf_exempt
def subtract(request):
    if request.method == 'POST':
        if post_data(request) != False:
            first_number, second_number = post_data(request)
            answer = first_number - second_number
            return JsonResponse({'answer': answer})
    return JsonResponse({'error': 'Invalid Request'})


@csrf_exempt
def multiply(request):
    if request.method == 'POST':
        if post_data(request) != False:
            first_number, second_number = post_data(request)
        answer = first_number * second_number
        return JsonResponse({'answer': answer})
    return JsonResponse({'error': 'Invalid Request'})


@csrf_exempt
def divide(request):
    if request.method == 'POST':
        if post_data(request) != False:
            first_number, second_number = post_data(request)
            if second_number == 0:
                return JsonResponse({'error': 'Division by zero'})
            answer = first_number / second_number
            return JsonResponse({'answer': answer})
    return JsonResponse({'error': 'Invalid Request'})
