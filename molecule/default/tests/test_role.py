import pytest

import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('name', [
  ('unattended-upgrades'),
])
def test_packages_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed


@pytest.mark.parametrize('file,user,group,mode', [
  ('20auto-upgrades', 'root', 'root', 0o644),
  ('50unattended-upgrades', 'root', 'root', 0o644),
])
def test_config_files_exist(host, file, user, group, mode):
    config = host.file('/etc/apt/apt.conf.d/' + file)
    assert config.exists
    assert config.is_file
    assert config.user == user
    assert config.group == group
    assert config.mode == mode
