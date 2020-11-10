from kubragen.consts import PROVIDER_GOOGLE, PROVIDERSVC_GOOGLE_GKE
from kubragen.provider import Provider


class ProviderGoogleGKE(Provider):
    def __init__(self):
        super().__init__(PROVIDER_GOOGLE, PROVIDERSVC_GOOGLE_GKE)
