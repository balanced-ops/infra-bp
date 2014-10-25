# infra-bp

**TOC**

- [Design](#Design)
- [Setup](#setup)
    - [Roles](#roles)
- [Hacking](#hacking)
    - [pypi](#pypi)

## Design

design of `infra-bp`:

```
infra-bp
├── atlas
├── formations
├── group_vars
├── inventories
├── lookup_plugins
├── meta
├── provisioning
├── roles
├── vars
```

infra-bp holds all balancedpayments (tokenized environment) level configurations, playbooks, and
applications (not services). 

if you desire to configure services, you might be interested in `infra-global`.

## atlas

The atlas is a `confu` helper utility that helps expedite development
of cloudformation patterns using troposphere. It achieves this by
exposing methods requiring a troposphere template argument and mutate
that template with commonly used cfn patterns in troposphere
(parameters, etc).

The atlas' primary purpose is annotate the troposphere template with
contextually correct common parameters and variables because it's
responsible for maintaing an up-to-date vpc network layout
(i.e. subnets, internet gateways, etc).

## formations

formations are configuration/code files that can be used to
materialize virtualized hardware (currently limited to just AWS) for a
particular service exposed by this repository.

they are typically implemented in troposphere named after the
functional role agnostic of the service they provide.

BAD formation: `formations/postgresql.py`
GOOD formation: `formations/db.py`

there's also typically an `all.py` formation that will materialize and
"form" all the formations -- re-materializing *all* services and
applications provided in this repository.

formations make heavy use of the `atlas` to know where to materialize
a particular service or application.

after the service or app is materialized via `formations`, the machinery
uses ansible to configure the newly formed nodes.

## inventories

inventories are an ansible concept that has been type coerced into
infrastructure service discovery. an inventory can be tied to a
specific region and currently uses different aws profiles for
different types of inventories.

currently, they just query the current infrastructure, materialized
via `formations` above, to return all available "nodes" in a
particular inventory.

inventories are tighly coupled to materialized `formations`, since
the `formations` machinery creates metadata tags (currently
AWS tags) to aid in inventory service discovery.

## roles

these are ansible roles that aid in the configuration of materialized
nodes through `formations`.

## vars

vars are configuration variables that are typically shared across all platform. They
are third party service API keys, ntp domains, user ssh keys, etc.

they have the same precedence in this repository's ansible playbooks.

it is important to note that this repository's default variables that
can be **optionally used as a default** when embedding into a parent
`infra-xxxx` (typically to consistently share variables, etc)

## provisioning

this is an ansible playbook to package this repository in a localhost
agnostic fashion and upload it to s3 for `formations` to pull and
execute when configuring a newly materialized node.

it is required because virtualenvs system paths differ when the
developers are on different host systems and the packaging code
provided by `confu` is linux specific (ubuntu).

See [Building a configuration](#building-a-configuration) for how to do this.

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

## Building a configuration

```bash
(infra-bp)$ pypi_username=user pypi_password=pass vagrant provision infra-global
(infra-bp)$ vagrant ssh infra-global -c "source ~/infra/bin/activate && cd ~/infra-global/ && confu pkg clean && confu pkg build"
(infra-bp)$ confu --region=us-east-1 pkg archive
```

