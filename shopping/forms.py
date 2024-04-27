from django import forms
from .models import Item

class AddItem(forms.ModelForm):
    """
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
    For editing items already made, allows users to edit the image, name, price, and description of an item.

    Args:
        model (Model): the Item model from shopping's models.py.
        fields (list): a list of fields that can be edited in the form. Image, name, price, and description. Should be pre-populated with the current values of the item.
    """
    class Meta:
        model = Item
        fields = ['image', 'name', 'price', 'description'] #same stuff, just lets you edit it