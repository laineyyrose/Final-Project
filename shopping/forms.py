from django import forms
from .models import Item, Comment, Post

# WORD TO THE WISE: If you use an imagefield in any of your forms, 
# be sure to include the 'enctype="multipart/form-data"' attribute in the form tag in your template!

class AddItem(forms.ModelForm):
    """
    Author: Andy
    A Django form for creating and updating item objects. 
    Allows users to create or update an item with an image, name, price, and description.

    Attributes:
        model (Model): The Django model this form is linked to: Item.
        fields (list): A list specifying the model fields that should be included in the form. Image, name, price, and description.
    """

    class Meta:
        model = Item  # Specifies the Django model to create or update
        fields = ['image', 'name', 'price', 'description']  # Specifies the fields to include in the form

class EditItem(forms.ModelForm):
    """
    Author: Andy
    For editing items already made, allows users to edit the image, name, price, and description of an item.

    Args:
        model (Model): the Item model from shopping's models.py.
        fields (list): a list of fields that can be edited in the form. Image, name, price, and description. Should be pre-populated with the current values of the item.
    """
    class Meta:
        model = Item
        fields = ['image', 'name', 'price', 'description'] #same stuff, just lets you edit it
        widgets = {'image': forms.ClearableFileInput(attrs={'class': 'form-control',}), 
                   'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What your item is (Max 50 characters.)', 'maxlength' : '50',}), 
                   'price': forms.NumberInput(attrs={'class': 'itemPrice form-control', 'placeholder': 'Price of item'}), 
                   'description': forms.Textarea(attrs={'class': 'form-control', 
                                                        'placeholder': 'Describe your item here... (Max 250 characters.)', 
                                                        'maxlength' : '250', 
                                                        'style': 'height: 100px',
                                                        }), }

class AddComment(forms.ModelForm):
    """
    Author: Andy
    A form for adding comments to an item. Allows users to add a comment to an item.

    model (Model): the Item model from shopping's models.py.
        fields (list): a list of fields that can be edited in the form. Image, name, price, and description. Should be pre-populated with the current values of the item.
    """
    class Meta:
        model = Comment
        fields = ['comment'] #just the comment & whether if it's a reply, the user and item are auto-filled
        
from django import forms
from .models import Post

class PostForm(forms.ModelForm):    
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body', 'header_image')

        widget = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
    
