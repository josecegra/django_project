from django.shortcuts import render, redirect

from .forms import HashtagForm

from django.http import HttpResponse, HttpResponseRedirect


from .apps import HashtagAppConfig, get_hashtags

# Create your views here.


def upload_view(request, *args,**kwargs):
    form = HashtagForm(request.POST or None, request.FILES or None)
    instance = form.instance
    print(request.POST)
    print(request.FILES)


    if form.is_valid():
        print("hey")
        instance = form.save(commit=False)
        instance.save()
        context = {"instance":instance,"form":form}
        #redirect
        return render(request, "hashtags/display_image.html", context)


    context = {"instance":instance,"form":form}
    return render(request, "hashtags/upload.html", context)

def result_view(request):



    context = {
        'form': form
    }
    return render(request, "hashtags/create_hashtags.html", context)


def hashtag_create_view(request):

    if request.method == 'POST':
        form = HashtagForm(request.POST or None)
        if form.is_valid():
            form.save()
            #form = HashtagForm()
            input_text = form.cleaned_data['input_text']
            #print(input_text)
            df = get_hashtags(input_text)
            print(df.head())
            context = {
                'header_table': df.columns,
                'df_values':df.values[:100]
            }

            #redirect
            return render(request, "hashtags/result.html", context)

    else:
        form = HashtagForm()
        print("other")

    context = {
        'form': form
    }
    return render(request, "hashtags/create_hashtags.html", context)




    
