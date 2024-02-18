
from django import forms

class HomeForm(forms.Form):
    num = forms.IntegerField()
    
    def clean_num(self):
        numpics = self.cleaned_data['num']
        if numpics < 1 or numpics > 5:
            raise forms.ValidationError('Number of pictures must be 1 - 5')
        return numpics