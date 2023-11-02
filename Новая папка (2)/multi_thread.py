from socket import *
import threading
import time
# Создаем функцию для обработки клиентского запроса в отдельном потоке
def handle_client(connectionSocket, addr):
    try:
        # Получаем запрос от клиента
        message = connectionSocket.recv(1024).decode()
        # Извлекаем имя запрашиваемого файла из запроса
        filename = message.split()[1].lstrip('/')
        # Открываем файл и читаем его содержимое
        with open(filename, 'r', encoding='utf-8') as f:
            outputdata = f.read()
        time.sleep(10)
        # Отправляем HTTP-заголовок и содержимое файла клиенту
        connectionSocket.send('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n'.encode())
        connectionSocket.send(outputdata.encode())

        # Закрываем соединение с клиентом
        connectionSocket.close()

    except IOError:
        # Если файл не найден, отправляем HTTP-заголовок и сообщение об ошибке 404
        connectionSocket.send('HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n'.encode())
        connectionSocket.send('<html><body><h1>404 Not Found</h1></body></html>'.encode())
        # Закрываем соединение с клиентом
        connectionSocket.close()

# Задаем порт, на котором будет работать сервер
serverPort = 80

# Создаем TCP-сокет для сервера
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
print('Servet started...')

# Бесконечный цикл для обработки входящих соединений
while True:
    # Ждем входящее соединение
    connectionSocket, addr = serverSocket.accept()
    print('New client connected:', addr)

    # Создаем новый поток для обработки запроса клиента
    client_thread = threading.Thread(target=handle_client, args=(connectionSocket, addr))
    client_thread.start()


