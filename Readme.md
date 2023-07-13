[![tests](https://github.com/boutetnico/ansible-role-unattended-upgrades/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-unattended-upgrades/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.unattended_upgrades-blue.svg)](https://galaxy.ansible.com/boutetnico/unattended_upgrades)

ansible-role-unattended-upgrades
================================

This role installs and configures unattended-upgrades.

Requirements
------------

Ansible 2.10 or newer.

Supported Platforms
-------------------

- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Debian - 12 (Bookworm)](https://wiki.debian.org/DebianBookworm)
- [Ubuntu - 20.04 (Focal Fossa)](http://releases.ubuntu.com/20.04/)
- [Ubuntu - 22.04 (Jammy Jellyfish)](http://releases.ubuntu.com/22.04/)

Role Variables
--------------

| Variable                     | Required | Default               | Choices   | Comments                                 |
|------------------------------|----------|-----------------------|-----------|------------------------------------------|
| unattended_dependencies      | true     | `unattended-upgrades` | string    |                                          |
| unattended_package_blacklist | true     | `[]`                  | list      |                                          |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - role: ansible-role-unattended-upgrades

Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
