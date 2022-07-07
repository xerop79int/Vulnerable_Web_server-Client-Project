def check_request(request):
    if not "GET" in request or not "HTTP/1.1" in request:
        return "request not supported"
    else:
        response = """HTTP/1.1 200

        <!DOCTYPE html> 
        <head> 
            <title> Hello, world! </title> 
        </head> 
        <body> 
        Hello world! 
        and Comma goes, Nizza?
        </body> 
        </html>"""

        return response