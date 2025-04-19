#Importing the forms module so we can create our forms
from django import forms
#Importing the Comment model from the models.py file in the same directory 
from .models import Comment

#Creating a form for the email sharing of a post we use tailwind css for the styling of the form
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

#Creating a form for the comments we use tailwind css for the styling of the form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body'] 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-300',
            'placeholder': 'Your name'
        })

        self.fields['email'].widget.attrs.update({
            'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-300',
            'placeholder': 'Your email address'
        })

        self.fields['body'].widget.attrs.update({
            'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-300',
            'placeholder': 'Write your comment here...'
        })

