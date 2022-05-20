"""Flask"""
import json
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException
from nornir import InitNornir

app = Flask(__name__)

from services.devices import (get_inventory, add_device, delete_device, get_device_by_name,
                              get_device_interfaces, get_device_interfaces_ip, get_device_facts)
from services.config import get_config_by_device


def init_nornir():
    """Init Nornir"""
    app.config['nr'] = InitNornir(config_file="fastprod/inventory/config.yaml")


init_nornir()


@app.route('/')
def welcome():
    """Welcome"""
    return jsonify(env='DEV', name='Fastprod_backend', version='1.0.0')


@app.errorhandler(HTTPException)
def handle_exception(error):
    """Handle HTTP exceptions."""
    # start with the correct headers and status code from the error
    response = error.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": error.code,
        "name": error.name,
        "description": error.description,
    })
    response.content_type = "application/json"
    return response


@app.route("/devices", methods=["GET", "POST"])
def devices():
    """Devices endpoint"""
    if request.method == "GET":
        devices_list = get_inventory()
        return jsonify(total_count=len(devices_list), device=devices_list)

    if request.method == "POST":
        data = request.get_json()
        new_device = add_device(data)
        return jsonify(device=new_device)


@app.route("/devices/<device_name>", methods=['GET', 'DELETE'])
def device_by_name(device_name):
    """Device by name endpoint"""
    if request.method == 'GET':
        device = get_device_by_name(device_name)
        return jsonify(device=device)
    if request.method == 'DELETE':
        device = get_device_by_name(device_name)
        delete_device(device)
        return jsonify(message="Device deleted")


@app.route("/devices/<device_name>/interfaces", methods=['GET'])
def get_interfaces(device_name):
    """Get device interfaces"""
    if get_device_by_name(device_name) and request.method == 'GET':
        device = get_device_by_name(device_name)
        interfaces = get_device_interfaces(device)
    return jsonify(interfaces=interfaces)


@app.route("/devices/<device_name>/interfaces/ip", methods=['GET'])
def get_interfaces_ip(device_name):
    """Get device interfaces ip"""
    if request.method == 'GET' and get_device_by_name(device_name):
        device = get_device_by_name(device_name)
        interfaces_ip = get_device_interfaces_ip(device)
    return jsonify(interfaces_ip=interfaces_ip)


@app.route("/devices/<device_name>/facts", methods=['GET'])
def get_facts(device_name):
    """ Get device facts"""
    if request.method == 'GET' and get_device_by_name(device_name):
        device = get_device_by_name(device_name)
        facts = get_device_facts(device)
        print(facts)
    return jsonify(facts=facts)


@app.route("/devices/<device_name>/config", methods=['GET'])
def get_config(device_name):
    """Get device config"""
    if request.method == 'GET' and get_device_by_name(device_name):
        device = get_device_by_name(device_name)
        config = get_config_by_device(device)
    return jsonify(config=config)
