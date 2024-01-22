from jsonschema import Draft7Validator
from flask import jsonify
import json
from schema._init_ import *

def isValidationError(dataInstance, schema):
    GereralSchemas = Draft7Validator(schema)
    validationErrors = []
    for error in sorted(GereralSchemas.iter_errors(dataInstance), key=str):
        validationErrors.append(error.message)
    if not validationErrors:
        return False
    return validationErrors

def successRes(msg=None, key=None, value=None):
    out = {"status": 'success',
           "message": msg if msg else 'Success Msg'}
    if key and value:
        out.update({"data": {
            key: value
        }
        })
    return jsonify(out)


def failureRes(msg=None, errors=None):
    out = {
        "status": 'failure',
        "message": msg if msg else 'Failure Msg'
    }
    if errors:
        out.update({'errors': errors})
    return jsonify(out)

def getData(request):
    try:
        return json.loads(request.data)
    except Exception as e:
        return None