from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world! <a href='/contacts'>Контакты</a>")

def contacts(request):
    return HttpResponse("Email: mefisto40000x@gmail.com <a href='/'>Назад</a>")