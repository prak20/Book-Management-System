from django.conf.urls import url
from Bookapp import views
urlpatterns=[
url(r'view-books',views.viewBooks),
url(r'^edit-book',views.editBook),
url(r'^search-book',views.searchBook),
url(r'^new-book',views.newBook),
url(r'^delete-book',views.deleteBook),
url(r'^add',views.add),
url(r'^search',views.search),
url(r'^edit',views.edit),
url('login',views.userLogin),
url('logout',views.userLogout),
]
