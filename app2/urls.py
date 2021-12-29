from django.urls.conf import path
from . import views


urlpatterns= [
    path('',views.admin ,name = 'admin'),
    path('delete/<id>',views.delete ,name = 'delete'),
    path('create',views.create ,name = 'create'),
    path('update/<id>',views.update ,name = 'update'),
    path('search',views.search ,name = 'search'),
    path('adminlogout',views.adminlogout ,name = 'adminlogout'),

]