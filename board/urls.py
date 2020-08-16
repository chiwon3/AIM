from django.urls import path
from .views import board,create,detail,update,delete,comment_create,comment_delete

urlpatterns = [
    path('board/',board, name="board" ),
    path('create/',create, name="create" ),
    path('detail/<int:post_id>',detail, name="detail" ),
    path('update/<int:post_id>',update, name="update" ),
    path('delete/<int:post_id>',delete, name="delete" ),
    path('comment_create/<int:post_id>',comment_create, name="comment_create" ),
    path('comment_delete/<int:post_id>/<int:com_id>', comment_delete, name="comment_delete"),
]
