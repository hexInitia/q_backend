def check_request_param(request, param):
    if param in request.query_params.keys():
        return request.query_params[param]
    return None