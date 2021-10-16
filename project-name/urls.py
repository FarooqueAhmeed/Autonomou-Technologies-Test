


from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url


# for swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Django-API-boilerplate ",
      default_version='v1',
      description="Django-API-boilerplate",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="zizopixels11@gmail.com"),
      license=openapi.License(name="zizopixels"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),



    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # for addding basic login log out func
    path('api-auth/', include('rest_framework.urls')),

    # default basic authentication login,logOut,reset, and confirm email
    # api/rest-auth/ ^password/reset/$ [name='rest_password_reset']
    # api/rest-auth/ ^password/reset/confirm/$ [name='rest_password_reset_confirm']
    # api/rest-auth/ ^login/$ [name='rest_login']
    # api/rest-auth/ ^logout/$ [name='rest_logout']
    # api/rest-auth/ ^user/$ [name='rest_user_details']
    # api/rest-auth/ ^password/change/$ [name='rest_password_change']
    path('api/rest-auth/', include('rest_auth.urls')),

    # from django-allauth pak.. for registration
    path('api/rest-auth/registration/', include('rest_auth.registration.urls')),

]
