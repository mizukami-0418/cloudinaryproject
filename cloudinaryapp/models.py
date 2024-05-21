from django.db import models
from cloudinary.models import CloudinaryField

class Photo(models.Model):
    """
    画像を保存するためのDjangoモデル。

    このモデルは、タイトルとCloudinaryに保存される画像を持ちます。

    Attributes:
        title (str): 画像のタイトル。最大100文字。
        image (CloudinaryField): Cloudinaryに保存される画像。
    """

    title = models.CharField(max_length=100)
    image = CloudinaryField('image')

    def __str__(self):
        """
        モデルインスタンスの文字列表現を返します。

        Returns:
            str: 画像のタイトル。
        """
        return self.title

# imageを複数選択しアルバムを作成するモデル
class Album(models.Model):
    name = models.CharField(max_length=100)
    photos = models.ManyToManyField(Photo)

    def __str__(self):
        return self.name