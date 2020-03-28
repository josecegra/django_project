from django import forms


from .models import Hashtag, Image


class HashtagForm(forms.ModelForm):    
    class Meta:
        model = Hashtag
        fields = [
            'input_text'        ]


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = [
            'image'        ]



class RawHashtagForm(forms.Form):
    title       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Your description",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "rows": 20,
                                    'cols': 120
                                }
                            )
                        )
    price       = forms.DecimalField(initial=199.99)