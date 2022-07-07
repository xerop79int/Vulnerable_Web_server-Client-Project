import os

def check_request(request):

    command = request
    command = command.partition('\n')[0]

    if "add" in request:
        response = Command(request)
        return response
    else:   
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

def savetoFile(command, filename):
    with open(filename, 'a') as f:
        f.write(command + "\n")
    
    f.close()

def escaped_utf8_to_utf8(s):
    s = s.replace("+", " ")
    res = b''; i = 0
    while i < len(s):
        if s[i] == '%':
            res += int(s[i+1:i+3], base=16).to_bytes(1, byteorder='big')
            i += 3
        else:
            res += s[i].encode()
            i += 1
    return res.decode('utf-8')

def readFromFile(filename):
    with open(filename, "r") as txt_file:
        return txt_file.readlines()



def Command(command):
    command = command.partition('\n')[0]
    command = command.split("&")[0].split("=")[1]
    command = escaped_utf8_to_utf8(command)


 
    savetoFile(command, "./tmp/command.txt")
    commands = readFromFile("./tmp/command.txt")
    command = '<br>'.join(commands)
    response = f"""HTTP/1.1 200

<!DOCTYPE html>
<body>
{command}
<form action="add" method="get"> 
<input type="text" name="input" placeholder="Type something" > 
<input type="submit" name="send" value="& #9166;" > 
</form>
</body>
</html>"""

    return response