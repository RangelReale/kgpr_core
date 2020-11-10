from kubragen.consts import PROVIDER_K3D, PROVIDERSVC_GENERIC
from kubragen.provider import Provider


class ProviderK3DGeneric(Provider):
    def __init__(self):
        super().__init__(PROVIDER_K3D, PROVIDERSVC_GENERIC)
