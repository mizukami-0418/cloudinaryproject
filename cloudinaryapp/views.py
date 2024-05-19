# views.py

from django.shortcuts import render, redirect
from .forms import PhotoForm
from .models import Photo

def upload_photo(request):
    """
    POSTリクエストを処理し、フォームから送信された画像をアップロードして保存する。
    フォームが有効であれば、写真リストページにリダイレクトする。
    GETリクエストの場合は、空のフォームを生成してアップロード画面を表示する。

    Parameters:
    - request: HTTPリクエストオブジェクト

    Returns:
    - HTTPレスポンスオブジェクト: アップロード画面のレンダリング結果を返す
    """
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo_list')
    else:
        form = PhotoForm()
    return render(request, 'cloudinaryapp/upload_photo.html', {'form': form})

def photo_list(request):
    """
    データベースからすべての写真オブジェクトを取得し、写真リストページに表示する。

    Parameters:
    - request: HTTPリクエストオブジェクト

    Returns:
    - HTTPレスポンスオブジェクト: 写真リストページのレンダリング結果を返す
    """
    photos = Photo.objects.all()
    return render(request, 'cloudinaryapp/photo_list.html', {'photos': photos})
