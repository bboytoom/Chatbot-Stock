import functools
from flask import request, abort


def validator_body(schema):
    """
    Decorator function that validates the endpoint body.
    """

    # Sub function
    def validation(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            content_type = request.headers.get('Content-Type')
            schema_event = schema()

            if content_type != 'application/json':
                return abort(400, 'Content-Type not supported!')

            errors = schema_event.validate(request.get_json())

            if errors:
                return abort(422, errors)

            return func(self, request.get_json(), *args, **kwargs)
        return wrapper
    return validation
