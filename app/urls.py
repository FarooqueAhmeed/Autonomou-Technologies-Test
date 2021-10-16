
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, AppViewSet



router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', AppViewSet, basename='App')
urlpatterns = router.urls
