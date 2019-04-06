from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hellow Wordl</h1>')

