def check_request(request):
    if not "GET" in request or not "HTTP/1.1" in request:
        return "request not supported"
    else:
        response = """HTTP/1.1 200

<!DOCTYPE html>
<body>
<form action="add" method="get"> 
<input type="text" name="input" placeholder="Type something" > 
<input type="submit" name="send" value="& #9166;" > 
</form>
</body>
</html>"""

        return response