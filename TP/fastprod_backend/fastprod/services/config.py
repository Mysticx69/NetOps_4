from api import app
from nornir_napalm.plugins.tasks import napalm_get


def get_config_by_device(device):
    """Get device config"""
    nr = app.config.get('nr')
    result = nr.filter(device_name=device.get('name')).run(task=napalm_get, getters=["get_config"])
    return result[device.get('name')][0].result.get('get_config')