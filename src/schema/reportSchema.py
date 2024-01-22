class ReportSchema():
    post = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "required": [
        "ip",
        "by"
    ],
    "properties": {
        "ip": {
            "$id": "#/properties/ip",
            "type": "string"
        },
        "by": {
            "$id": "#/properties/by",
            "type": "string"
        }
    },
    "additionalProperties": True
}