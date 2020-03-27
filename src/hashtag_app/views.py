from django.shortcuts import render, redirect

from .forms import HashtagForm

from .apps import HashtagAppConfig, get_hashtags

# Create your views here.

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

# def hashtag_create_view(request):

#     form = HashtagForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         #form = HashtagForm()
#         input_text = form.cleaned_data['input_text']
#         print(input_text)
#         print(get_hashtags(input_text))

        
#         #print(HashtagAppConfig.message)


#     context = {
#         'form': form
#     }
#     return render(request, "hashtags/create_hashtags.html", context)

#def hashtag_view(request, *args,**kwargs):
#    context = {"form":form}
#    return render(request, "home.html", {})


    
