from helpers.http_status import (
    ok,
    created,
    bad_request
)


def generic_success(data, status):
    return {'status': 'success', 'data': data}, status


def success_data(data):
    return generic_success(data, ok)


def created_data(data):
    return generic_success(data, created)


def generic_error(data):
    return {'status': 'error', 'data': data}, bad_request


def error_with_info(message, invalid_field):
    return {
        'status': 'error',
        'message': message,
        'invalid_field': invalid_field
    }, bad_request
