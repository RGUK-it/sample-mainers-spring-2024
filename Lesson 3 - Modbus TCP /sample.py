import socket, struct


# Функция для отправки запроса Modbus
def send_modbus_request(sock, request):
    sock.send(request)


# Функция для чтения holding registers
def read_holding_registers(ip, port, unit_id, start_address, num_registers):
    # Создаем сокс
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    print('log: законнектился')
    # Формируем запрос Modbus TCP
    transaction_id = 0x0001  # Произвольный идентификатор транзакции
    protocol_id = 0x0000  # Идентификатор протокола Modbus
    length = 6 + 2  # Длина данных

    # Формируем запрос Modbus

    request = struct.pack(">HHHBBHH", transaction_id, protocol_id, length, unit_id, 0x03, start_address, num_registers)
    print('log: сформировали запрос для модбас')
    send_modbus_request(sock, request)
    print('log: отправили запрос модбас')
    # Читаем ответ
    response = sock.recv(1024)
    print('log: ответ получен')
    # Обрабатываем ответ и извлекаем значения регистров
    data = response[9:]  # Отбрасываем заголовок Modbus
    values = struct.unpack(f">{num_registers}H", data)

    # Закрываем сокс
    sock.close()

    return values


# Пример использования
if __name__ == "__main__":
    ip = "127.0.0.1"  # IP-адрес сервера Modbus
    port = 502  # Порт сервера Modbus
    unit_id = 1  # Идентификатор устройства Modbus
    start_address = 0  # Начальный адрес чтения регистров хранения
    num_registers = 10  # Количество регистров для чтения

    values = read_holding_registers(ip, port, unit_id, start_address, num_registers)
    print("Значения регистров хранения:", values)
