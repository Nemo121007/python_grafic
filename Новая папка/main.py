from socket import *
from ssl import *
import base64

context = create_default_context()
msg = "Hello World!"
endmsg = "\r\n.\r\n"

mailserver = "smtp.gmail.com"
port = 465

sender_username = "sva.gashkov@gmail.com"
sender_password = "veqvdjvcswaarpzb"

with create_connection((mailserver, port)) as sock:
    with context.wrap_socket(sock, server_hostname=mailserver) as clientSocket:
        heloCommand = 'HELO Alice\r\n'

        clientSocket.send(heloCommand.encode())

        recv = clientSocket.recv(1024).decode()

        print(recv)
        base64_str = ("\0" + sender_username + "\0" + sender_password).encode()
        base64_str = base64.b64encode(base64_str)
        authMsg = "AUTH PLAIN ".encode() + base64_str + "\r\n".encode()
        # print(authMsg)
        clientSocket.send(authMsg)
        recv_auth = clientSocket.recv(1024)
        print("from auth: " + recv_auth.decode())

        clientSocket.send(("MAIL FROM:<" + sender_username + ">\r\n").encode())
        recv = clientSocket.recv(1024).decode()
        print("from mail from: " + recv)

        clientSocket.send(("RCPT TO:<" + sender_username + ">\r\n").encode())
        recv = clientSocket.recv(1024).decode()
        print("from rcpt to: " + recv)

        clientSocket.send("DATA\r\n".encode())
        recv = clientSocket.recv(1024).decode()
        print(recv)
        clientSocket.send(("Subject:Networks\r\n").encode())
        clientSocket.send(("Content-Type: multipart/mixed; boundary=frontier\r\n").encode())
        clientSocket.send(("--frontier\r\n").encode())
        clientSocket.send(("Content-Type: text/plain;\r\n").encode())
        clientSocket.send((msg + '\r\n').encode())
        clientSocket.send(("--frontier\r\n").encode())
        clientSocket.send(("Content-Transfer-Encoding:base64\r\n").encode())
        clientSocket.send(("Content-Type: image/jpg; name=picture.jpg\r\n\r\n").encode())
        with open("picture.jpg", "rb") as image:
                clientSocket.send(base64.b64encode(image.read() + '\r\n'.encode()))
                image.close()
        clientSocket.send(endmsg.encode())
        recv = clientSocket.recv(1024).decode()
        print(recv)

        clientSocket.send("QUIT\r\n".encode())
        recv = clientSocket.recv(1024).decode()
        print(recv)
        clientSocket.close()