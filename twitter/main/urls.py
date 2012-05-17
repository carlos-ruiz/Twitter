from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'main.views.LoginRequest', name='LoginRequest'),
    url(r'^home/$', 'main.views.LoginRequest', name='home'),
    url(r'^profile/$', 'main.views.profile', name='profile' ),
    url(r'^account/$', 'main.views.account', name='account' ),
    url(r'^edit/$', 'main.views.editProfile', name='editProfile'),
    url(r'^newTweet/$', 'main.views.newTweet', name='newTweet'),
    url(r'^register/$', 'main.views.Registration', name='Registration'),
    url(r'^accounts/login/$', 'main.views.LoginRequest', name='LoginRequest'),
    url(r'^logout/$', 'main.views.LogoutRequest', name='LogoutRequest' ),

    url(r'^resetpassword/$', 'django.contrib.auth.views.password_reset', name='resetpassword'),
    url(r'^resetpassword/passwordsent$', 'django.contrib.auth.views.password_reset_done', name='resetpasswordsent'),
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', name='resetpasswordconfirm'),
    url(r'^reset/done$', 'django.contrib.auth.views.password_reset_complete', name='resetdone'),

    )