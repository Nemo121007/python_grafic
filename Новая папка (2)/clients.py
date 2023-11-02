import socket
import threading

def send_request():
    # адрес сервера и порт
    server_address = ('localhost', 80)

    # создаем TCP-сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # устанавливаем соединение
    client_socket.connect(server_address)

    # формируем HTTP-запрос
    http_request = 'GET /Lab1.html HTTP/1.1\r\nHost: localhost\r\n\r\n'

    # отправляем запрос серверу
    client_socket.send(http_request.encode())

    # получаем ответ от сервера
    response = b''
    while True:
        data = client_socket.recv(4096)
        if not data:
            break
        response += data
    # закрываем соединение
    client_socket.close()

    # разбиваем ответ на заголовок и содержимое
    header, content = response.split(b'\r\n\r\n', 1)

    # распечатываем содержимое файла
    print(content.decode())


# Создаем список потоков
threads = []
# Запускаем 10 потоков-клиентов
for i in range(10):
    thread = threading.Thread(target=send_request)
    thread.start()
    threads.append(thread)

# Ждем завершения всех потоков
for thread in threads:
    thread.join()