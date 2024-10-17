from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)

from .viewsets import owner_viewset, tenant_viewset
from .viewsets.user import user_viewset, login_viewset
from .viewsets.property import visit_demand_viewset, property_viewset, location_demand_viewset
from .viewsets.transaction import subscription_viewset, payment_viewset

schema_view = get_schema_view(
    openapi.Info(
        title="YELEMANCI API",
        default_version='v1.4',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register(r'properties', property_viewset.PropertyViewSet, basename='properties')
router.register(r'tenants', tenant_viewset.TenantViewSet, basename='tenants')
router.register(r'owners', owner_viewset.OwnerViewSet, basename='owners')
router.register(r'users', user_viewset.UserViewSet, basename='users')
router.register(r'visit-demands', visit_demand_viewset.VisitDemandViewSet, basename='visit_demands')
router.register(r'location-demands', location_demand_viewset.LocationDemandViewSet, basename='location_demands')
router.register(r'payments', payment_viewset.PaymentViewSet, basename='payments')
router.register(r'subscriptions', subscription_viewset.SubscriptionViewSet, basename='subscriptions')

urlpatterns = [

    path('', include(router.urls)),
    path('otp/verify/', user_viewset.OtpVerifyViewSet.as_view({'post': 'create'}), name='verify-otp'),
    path('login/', login_viewset.LoginViewSet.as_view({'post': 'login'}), name='login'),
    path('otp/regenerate/', user_viewset.OtpVerifyViewSet.as_view({'post': 'regenerate_otp'}), name='otp-regenerate'),
    path('api-auth/', include('rest_framework.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
