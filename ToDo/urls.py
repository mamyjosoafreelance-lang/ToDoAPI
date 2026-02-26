from rest_framework.routers import DefaultRouter
from .models import ToDo
from .views import ToDoViewSet

router = DefaultRouter()
router.register(r'api', ToDoViewSet)

urlpatterns = router.urls