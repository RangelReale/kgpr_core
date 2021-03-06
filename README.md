# KubraGen Providers: Core

[![PyPI version](https://img.shields.io/pypi/v/kgpr_core.svg)](https://pypi.python.org/pypi/kgpr_core/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/kgpr_core.svg)](https://pypi.python.org/pypi/kgpr_core/)

kgpr_core is a collection of core providers for [KubraGen](https://github.com/RangelReale/kubragen). 

[KubraGen](https://github.com/RangelReale/kubragen) is a Kubernetes YAML generator library that makes it possible to generate
configurations using the full power of the Python programming language.

* Website: https://github.com/RangelReale/kgpr_core
* Repository: https://github.com/RangelReale/kgpr_core.git
* Documentation: https://kgpr_core.readthedocs.org/
* PyPI: https://pypi.python.org/pypi/kgpr_core

### Provider

* Google GKE: ```kgpr_core.google.gke.provider.ProviderGoogleGKE```
* Amazon EKS: ```kgpr_core.amazon.eks.provider.ProviderAmazonEKS```
* DigitalOcean Kubernetes: ```kgpr_core.digitalocean.kubernetes.provider.ProviderDigitalOceanKubernetes```
* KIND: ```kgpr_core.kind.generic.provider.ProviderKINDGeneric```
* K3D: ```kgpr_core.k3d.generic.provider.ProviderK3DGeneric```

## Author

Rangel Reale (rangelreale@gmail.com)
