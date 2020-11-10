from kgpr_core.amazon.eks.provider import ProviderAmazonEKS
from kgpr_core.digitalocean.kubernetes.provider import ProviderDigitalOceanKubernetes
from kgpr_core.google.gke.provider import ProviderGoogleGKE

p_google = ProviderGoogleGKE()
p_amazon = ProviderAmazonEKS()
p_digitalocean = ProviderDigitalOceanKubernetes()
