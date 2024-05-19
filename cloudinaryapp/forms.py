# forms.py

from django import forms
from .models import Photo

class PhotoForm(forms.ModelForm):
    """
    PhotoFormは、写真をアップロードするためのフォームを定義します。

    このフォームは、Djangoのモデルフォームを拡張しており、Photoモデルに関連付けられています。
    titleとimageの2つのフィールドを持ちます。

    Attributes:
        model (Model): フォームが基づいているDjangoモデルであり、Photoモデルです。
        fields (list): フォームに表示されるフィールドのリストです。ここでは、タイトルと画像が含まれています。
    """

    class Meta:
        model = Photo
        fields = ['title', 'image']