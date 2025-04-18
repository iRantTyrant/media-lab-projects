from django import forms

class emailPostForm(forms.Form):
    name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={
        'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-300 placeholder-gray-400',
        'placeholder': 'iRant Tyrant'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-300',
        'placeholder': 'irant@mail.com'
    }))
    to = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-300',
        'placeholder': 'friendsmail@mail.com'
    }))
    comments = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-300',
        'rows': 4,
        'placeholder': 'Write your comments here...'
    }))