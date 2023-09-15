from django.urls import path
from .views import home, article, createpost, updatepost, deletepost, category

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('article/<int:pk>', article.as_view(), name='article'),
    path('create', createpost.as_view(), name='create'),
    path('article/edit_post/<int:pk>', updatepost.as_view(), name='update_post'),
    path('article/delete_post/<int:pk>', deletepost.as_view(), name='delete_post'),
    path('category/<str:id>', category, name='category')

]
