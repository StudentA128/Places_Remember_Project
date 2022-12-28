from django.forms import ModelForm
from django.forms import TextInput
from django.forms import Textarea

from .models import Places


class PlacesForm(ModelForm):
    class Meta:
        model = Places
        fields = [
            "place_title",
            "place_description",
            "place_latitude",
            "place_longitude",
            "user_id",
        ]
        widgets = {
            "place_title": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Название места",
                    "id": "place-title-id",
                }
            ),
            "place_description": Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Комментарий об этом месте",
                    "id": "place-description-id",
                }
            ),
            "place_latitude": TextInput(
                attrs={
                    "class": "form-control",
                    "id": "lat",
                    "readonly": "readonly",
                }
            ),
            "place_longitude": TextInput(
                attrs={
                    "class": "form-control",
                    "id": "lng",
                    "readonly": "readonly",
                }
            ),
            "user_id": TextInput(
                attrs={
                    "type": "hidden",
                    "id": "user",
                    "readonly": "readonly",
                }
            ),
        }
