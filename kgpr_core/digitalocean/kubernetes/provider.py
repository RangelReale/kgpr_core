from kubragen.consts import PROVIDER_DIGITALOCEAN, \
    PROVIDERSVC_DIGITALOCEAN_KUBERNETES
from kubragen.provider import Provider


class ProviderDigitalOceanKubernetes(Provider):
    def __init__(self):
        super().__init__(PROVIDER_DIGITALOCEAN, PROVIDERSVC_DIGITALOCEAN_KUBERNETES)
