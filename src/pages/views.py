from django.http import HttpResponse
from django.shortcuts import render


def result_view(request):
    return 

# Create your views here.
def home_view(request, *args,**kwargs):
    print(request.user)
    #return HttpResponse("<h1>Hello world<h1>")
    return render(request, "home.html", {})

def about_view(request, *args,**kwargs):
    my_context = {
        "header_table":["Firstname","Lastname","Email"],
        "data": [["John","Doe","john@example.com"],
                 ["Mary","Moe","mary@example.com"],
                 ["July","Dooley","july@example.com"],
                 ["asdf","dfd","jsdfdfdly@example.com"]],
        "my_list":[1,4,3,5,6]
        }
    return render(request, "about.html", my_context)

def upload_view(request, *args,**kwargs):

    #form = Hashta

    if request.method == 'POST':
        uploaded_file = request.FILES['document']

        print(request.FILES)
        print(uploaded_file)

        #print(uploaded_file.name)



    return render(request, "upload.html", {})