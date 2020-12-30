from django.contrib import admin
from django.urls import path
from django.conf.urls import include
# from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic import TemplateView
from django.conf import settings   
from django.conf.urls.static import static
# from lionsclub.views import FacebookLogin, TwitterLogin, GitHubLogin, FacebookConnect, TwitterConnect, GitHubConnect

# from rest_auth.registration.views import (
#     SocialAccountListView, SocialAccountDisconnectView
# )

from rest_framework.schemas import get_schema_view # Filters api codes and descriptions
from rest_framework.documentation import include_docs_urls  # captures information from schema_view and provides doc


# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [

    # path('socialaccounts/', SocialAccountListView.as_view(), 
    # name='social_account_list'),

    # path('socialaccounts/(<pk>)/disconnect/', SocialAccountDisconnectView.as_view(),
    # name='social_account_disconnect'),

    path('admin/', admin.site.urls),
    path('api/', include('lionsclub.urls')),
    path('auth/', include('drf_social_oauth2.urls', namespace='drf')),
    # path('auth/', obtain_auth_token),
    # path('rest-auth/', include('rest_auth.urls')),

    # path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    # path('rest-auth/twitter/', TwitterLogin.as_view(), name='twitter_login'),
    # path('rest-auth/github/', GitHubLogin.as_view(), name='github_login'),

    # path('rest-auth/facebook/connect/', FacebookConnect.as_view(), name='fb_connect'),
    # path('rest-auth/twitter/connect/', TwitterConnect.as_view(), name='twitter_connect'),
    # path('rest-auth/github/connect/', GitHubConnect.as_view(), name='github_connect'),


    # path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), # It includes login and logout views for browsable API.
    path('docs/', include_docs_urls(title='ClubAPI')),
    path('schema', get_schema_view(
        title="BlogAPI",
        description="API for all BlogAPI ...",
        version="1.0.0"
    ), name = 'openapi-schema'),

    # JWT Tokens
    # path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

    # path('', TemplateView.as_view(template_name='index.html')), # Uncomment this line to run react UI.
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
