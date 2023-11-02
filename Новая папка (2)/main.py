from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#Подготавливаем сокет сервера
serverPort = 80 #порт сервера
serverSocket.bind(('', serverPort))                     #связываем сокет сервера с портом
serverSocket.listen(1)                                  #слушаем входящие запросы на соединение

#http://localhost/Lab1.html

while True:
    #Устанавливаем соединение
    print('Server started...')
    connectionSocket, addr = serverSocket.accept()
    #принимаем входящее соединение и создаем новый сокет для общения с клиентом
    try:
        message = connectionSocket.recv(1024).decode()
        #получаем данные от клиента
        filename = message.split()[1][1:]
        print(filename)
        f = open(filename, 'r', encoding='utf-8')
        outputdata = f.read()                           #читаем содержимое файла
        #Отправляем в сокет одну строку HTTP-заголовка
        connectionSocket.send('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n'.encode())
        #Отправляем содержимое запрошенного файла клиенту
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
    except IOError:
        #Отправляем ответ об отсутствии файла на сервере
        connectionSocket.send('HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n'.encode())
        connectionSocket.send('<html><body><h1>404 Not Found</h1></body></html>'.encode())
        #Закрываем клиентский сокет
        connectionSocket.close()
serverSocket.close()
