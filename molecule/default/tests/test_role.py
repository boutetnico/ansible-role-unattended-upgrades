import pytest


@pytest.mark.parametrize(
    "name",
    [
        ("unattended-upgrades"),
    ],
)
def test_packages_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed


@pytest.mark.parametrize(
    "file,user,group,mode",
    [
        ("20auto-upgrades", "root", "root", 0o644),
        ("50unattended-upgrades", "root", "root", 0o644),
    ],
)
def test_config_files_exist(host, file, user, group, mode):
    config = host.file("/etc/apt/apt.conf.d/" + file)
    assert config.exists
    assert config.is_file
    assert config.user == user
    assert config.group == group
    assert config.mode == mode


def test_auto_upgrades_config_content(host):
    config = host.file("/etc/apt/apt.conf.d/20auto-upgrades")
    assert 'APT::Periodic::Update-Package-Lists "1";' in config.content_string
    assert 'APT::Periodic::Unattended-Upgrade "1";' in config.content_string


def test_unattended_upgrades_config_content(host):
    config = host.file("/etc/apt/apt.conf.d/50unattended-upgrades")
    content = config.content_string
    assert "Unattended-Upgrade::Package-Blacklist" in content
    assert '"vim"' in content
    assert '"libc6"' in content
