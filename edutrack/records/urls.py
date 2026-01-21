from rest_framework.routers import DefaultRouter
from .views import AcademicRecordViewSet

router = DefaultRouter()
router.register('records', AcademicRecordViewSet)

urlpatterns = router.urls