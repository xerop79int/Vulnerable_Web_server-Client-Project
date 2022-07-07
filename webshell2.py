import os

# Reading the response from the server
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

#  Saving to the file
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

# Readin from the file
def readFromFile(filename):
    with open(filename, "r") as txt_file:
        return txt_file.readlines() 

# handling the command

def commandResponse(command):
    out = os.popen(command).read()
    return out

def Command(command):
    command = command.partition('\n')[0]
    command = command.split("&")[0].split("=")[1]
    command = escaped_utf8_to_utf8(command)
    
    if os.path.exists("./tmp/command.txt"):
        checkLastCommand = readFromFile("./tmp/command.txt")
        for i in range(len(checkLastCommand)-1, 0, -1):
            if "cd" in checkLastCommand[i]:
                if ">" in checkLastCommand[i]:
                    command = checkLastCommand[i].split(">")[1].strip() + ";" + command
                    break
    
    if os.path.exists("./tmp/command.txt"):
        checkLastCommand = readFromFile("./tmp/command.txt")
        checkLastCommand = checkLastCommand[-1]
        if "read" in checkLastCommand:
            command = 'echo "' + command + '"' 

    if "cd" in command and ";" in command:
        command_response = commandResponse(command)
        command = command.split(";")[0]
        savetoFile("Command=> " + command, "./tmp/command.txt")
    elif command == "read" and command == "Read":
        savetoFile("Command=> " + command, "./tmp/command.txt")
    else:
        savetoFile("Command=> " + command, "./tmp/command.txt")
        command_response = commandResponse(command)


    if command_response != "":
        savetoFile(command_response, "./tmp/command.txt")
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