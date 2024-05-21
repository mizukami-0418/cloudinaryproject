# forms.py

from django import forms
from .models import Photo, Album

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

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['name', 'photos']
        # CheckboxSelectMultipleウィジェットを使用し、チェックボックスのリストとして表示
        widgets = {
            'photos': forms.CheckboxSelectMultiple(),
        }