from django.shortcuts import render,HttpResponse

# Create your views here.
def unk(request):
    return render(request, "index_first.html")