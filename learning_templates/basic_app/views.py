from django.shortcuts import render

# Create your views here.
def index(request):
    mycontext = {"hello":"hari haran","number" : 89}
    return render(request,"basic_app/index.html",mycontext)

def other(request):
    return render(request,"basic_app/other.html")

def relative(request):
    return render(request,"basic_app/relative_url_template.html")