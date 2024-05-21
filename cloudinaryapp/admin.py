# admin.py

from django.contrib import admin
from .models import Photo

admin.site.register(Photo)
"""
Photoモデルの管理を行うための管理サイト設定。

このモジュールは、Djangoの管理サイトでPhotoモデルを編集・表示するための設定を提供します。
Photoモデルは、タイトルと画像を持つモデルであり、管理サイト上での操作を可能にします。
"""
admin.site.register(Album)