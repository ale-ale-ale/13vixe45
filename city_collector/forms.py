from django import forms


class CityForm(forms.Form):
    city = forms.CharField(label='City',
                           widget=forms.TextInput(attrs={'placeholder': 'Enter random city here'}), max_length=30,
                           required=False)
