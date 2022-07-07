def check_request(request):
    print(request)
    if not "GET" in request or not "HTTP/1.1" in request:
        return "request not supported"
    else:
        response = request

        return response