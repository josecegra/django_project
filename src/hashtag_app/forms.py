from django import forms


from .models import Hashtag


class HashtagForm(forms.ModelForm):
    #title       = forms.CharField(label='', 
    #                widget=forms.TextInput(attrs={"placeholder": "user1 user2 user3"}))
    # input_text = forms.CharField(
    #                     required=False, 
    #                     widget=forms.Textarea(
    #                             attrs={
    #                                 "placeholder": "user1 user2 user3",
    #                                 "class": "new-class-name two",
    #                                 "id": "my-id-for-textarea",
    #                                 "rows": 20,
    #                                 'cols': 120
    #                             }
    #                         )
    #                     )
    # price       = forms.DecimalField(initial=199.99)
    
    class Meta:
        model = Hashtag
        fields = [
            'input_text',
            'image'
        ]


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