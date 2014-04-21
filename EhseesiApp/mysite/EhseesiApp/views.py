# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")
  
def search(request):
    return HttpRequest.build_absolute_uri("EhseesiApp/search_page.html")
  
def results(request):
    return HttpRequest.build_absolute_uri("EhseesiApp/results_page.html")