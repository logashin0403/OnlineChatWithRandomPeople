import socket
from rmlib import GetIP

IP = GetIP()
print('\n\nServer started at {}: [loged.ddns.net]25565'.format(IP))

socket.setdefaulttimeout(0.1)
mass = []

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)

while True:
    try:
        conn, addr = sock.accept()
        mass.append(conn)
    except:
        pass

    for i in mass:
        try:
            i.send(''.encode())
        except:
            try:
                mass.remove(conn)
            except:
                pass

    for i in mass:
        try:
            data = i.recv(1024)
            if not data:
                pass
            else:
                data = data.decode('UTF-8')
                inum = 0
                #commands
                num = 0
                for i in data:
                    if(i == ":"):
                        num = inum+2
                    else:
                        inum += 1
                if(num == 0):
                    pass
                else:
                    #commands
                    msg = data[num:]
                    if(msg == "!restart"):
                        print('restarting')
                        for send in mass:
                            send.send("Server restarting...".encode('UTF-8'))
                        sock.close()
                        IP = GetIP()
                        print('\n\nServer started at {}:25565 [loged.ddns.net]'.format(IP))
                        socket.setdefaulttimeout(0.1)
                        mass = []
                        sock = socket.socket()
                        sock.bind((IP, 25565))
                        sock.listen(1)
                for i in mass:
                    i.send(data.encode('UTF-8'))
        except:
            pass
    data = ""
