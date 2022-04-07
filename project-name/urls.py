


from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

from app.views import *


# for swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter


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


# router = DefaultRouter()
# router.register('plan', PlanViewSet.as_view, basename='blogs')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),

    #path('', ApiOverview, name='home'),
    path('create/', add_app, name='add-app'),
    path('', view_apps, name='view-apps'),
    path('detail/<int:pk>/', app_detail, name='app-detail'),

    path('plan/', PlanViewSet, name='app-Plan'),
    path('plans/', view_plans, name='apps-Plans'),


    path('my_plans/', view_my_plans, name='apps-view_plans_created_by_me'),

    path('plan_detail/<int:pk>/', view_plan_detail, name='apps-view_plan_detail'),

    path('subscription_detail/<int:pk>/', view_subscription_detail, name='apps-view_subscription_detail'),







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
