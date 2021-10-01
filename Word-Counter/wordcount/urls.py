
from django.urls import path
from . import views
#from . import aboutme

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.homepage, name = 'home'),
    ## way to still work the page
    path('count/', views.count, name = 'count'),
    ## about me url
    path('aboutme/', views.aboutme, name = 'aboutme'),
]
