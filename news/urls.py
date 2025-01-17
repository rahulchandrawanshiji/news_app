from django.urls import path
from .import views 

urlpatterns = [
    path('',views.index,name="homepage"),
    path('signup',views.signup,name="Signup"),
    path('login',views.login,name="login"),
    path('about',views.about,name="About"),
    path('contact',views.contact,name="Contact"),
    path('search',views.search,name="Serch"),
    path('photo',views.photo,name="Photo"),
    path('video',views.vedio,name="Video"),
    path('state',views.state,name="State"),
    # path('Australia',views.Australia,name="Australia"),
    path('logout',views.logout,name="Logout"),
    path('country',views.country,name="country")
    
]
