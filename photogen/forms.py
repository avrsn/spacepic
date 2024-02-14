
from django import forms

class HomeForm(forms.Form):
    post = forms.IntegerField()
    
    def clean_post(self):
        numpics = self.cleaned_data['post']
        if numpics < 1 or numpics > 5:
            raise forms.ValidationError('Number of pictures must be 1 - 5')
        return numpics