from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ModuloPagos.views import (ConceptoViewSet, ProveedorViewSet, ComprobantePagoViewSet, PagoComprobanteViewSet, PagoPersonaViewSet, PrepagoViewSet)

router = DefaultRouter()
router.register(r'concepto-contable', ConceptoViewSet, basename='concepto-contable')
router.register(r'proveedor', ProveedorViewSet, basename='proveedor')
router.register(r'comprobante-pago', ComprobantePagoViewSet, basename='comprobante-pago')
router.register(r'pago-comprobante', PagoComprobanteViewSet, basename='pago-comprobante')
router.register(r'pago-persona', PagoPersonaViewSet, basename='pago-persona')
router.register(r'prepago', PrepagoViewSet, basename='prepago')


urlpatterns = [
    path('', include(router.urls)),
]
