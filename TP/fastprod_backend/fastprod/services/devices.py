"""Endpoints"""
from flask import (abort, make_response, jsonify)
from nornir import InitNornir
from utils.inventory import add_item_to_hosts_yaml, delete_item_from_hosts_yaml  #pylint: disable=import-error
from api import app  #pylint: disable=import-error
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get


def get_inventory():
    """Return devices from inventory"""
    hosts = app.config.get('nr').inventory.dict().get('hosts').keys()
    return list(
        map(lambda item: app.config.get('nr').inventory.dict().get('hosts').get(item), hosts))


def add_device(device):
    """Add device"""
    device = add_item_to_hosts_yaml(item=device)
    InitNornir()
    return device


def get_device_by_name(name):
    """Get device infos by name"""
    host = app.config.get('nr').inventory.hosts.get(name)
    if not host:
        abort(make_response(jsonify(message="device not found"), 404))
    return host.dict()


def delete_device(device):
    """ Delete device """
    try:
        delete_item_from_hosts_yaml(item=device)
        InitNornir()
    except Exception as error:
        abort(make_response(jsonify(message="Unable to delete this device", error=str(error)), 500))


def get_device_interfaces(device):
    """Get device interfaces"""

    nr = app.config.get('nr')
    result = nr.filter(device_name=device.get('name')).run(task=napalm_get,
                                                           getters=["get_interfaces"])
    print_result(result)
    interfaces = result[device.get('name')][0].result.get('get_interfaces')
    return list(map(lambda item: dict(name=item, **interfaces.get(item)), interfaces))


def get_device_interfaces_ip(device):
    """Get device interfaces ip"""

    nr = app.config.get('nr')
    result = nr.filter(device_name=device.get('name')).run(task=napalm_get,
                                                           getters=["get_interfaces_ip"])
    print_result(result)
    interfaces = result[device.get('name')][0].result.get('get_interfaces_ip')

    def transformer(item):
        ip_address = list(interfaces.get(item).get('ipv4').keys())[0]
        prefix_length = interfaces.get(item).get('ipv4').get(
            list(interfaces.get(item).get('ipv4').keys())[0]).get('prefix_length')
        return dict(name=item, ip=ip_address, prefix_length=prefix_length)

    return list(map(lambda item: transformer(item), interfaces))


def get_device_facts(device):
    """Get device facts"""
    print(device)
    nr = app.config.get('nr')
    result = nr.filter(device_name=device.get('name')).run(task=napalm_get, getters=["get_facts"])
    print_result(result)
    facts = result[device.get('name')][0].result.get('get_facts')
    print(facts)
    return facts