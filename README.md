# infra-bp

**TOC**

- [Setup](#setup)
    - [Roles](#roles)
- [Hacking](#hacking)
    - [pypi](#pypi)

## Setup

```bash
git clone --recursive git@github.com:balanced-ops/infra-bp.git
git submodule update --init --recursive
cd infra-bp
mkvirtualenv infra-bp
(infra-bp) pip install -r requirements.txt
```

### Roles

```bash
ansible-galaxy install -r requirements.yml -p `pwd`/roles
```

## Hacking

### pypi
