from django.http import HttpResponse 

# writing a simple
def index(request):
    return HttpResponse("Hello, world. You're at the polls index!")
