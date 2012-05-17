from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('main.views',
    url(r'^$', 'LoginRequest', name='LoginRequest'),
    url(r'^home/$', 'LoginRequest', name='home'),
    url(r'^profile/$', 'profile', name='profile' ),
    url(r'^account/$', 'account', name='account' ),
    url(r'^register/$', 'Registration', name='Registration'),
    url(r'^login/$', 'LoginRequest', name='LoginRequest'),
    url(r'^logout/$', 'LogoutRequest', name='LogoutRequest' ),
    url(r'^edit/$', 'editProfile', name='editProfile'),
    url(r'^newtweet$', 'newTweet', name='newTweet'),
    )