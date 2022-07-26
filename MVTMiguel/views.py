from django.http import HttpResponse


def welcome(request):
    return HttpResponse('Hola Bienvenido a mi primer MVT con Django')
