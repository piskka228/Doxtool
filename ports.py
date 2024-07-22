import socket
from datetime import datetime
from pystyle import Colors, Colorate, Center, Box

# Функция для сканирования порта
def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((ip, port))
        return True
    except:
        return False
    finally:
        s.close()

# Основная функция для сканирования диапазона портов
def port_scan(ip):
    print(Colorate.Horizontal(Colors.green_to_white, f"Сканирование {ip} на открытые порты (ожидаемое время ~2 минуты)..."))
    start_time = datetime.now()
    open_ports = []

    # Диапазон портов для сканирования
    for port in range(1, 1025):
        if scan_port(ip, port):
            open_ports.append(port)

    end_time = datetime.now()
    total_time = end_time - start_time

    print(Colorate.Horizontal(Colors.green_to_white, f"\nСканирование завершено за {total_time}\n"))
    
    if open_ports:
        print(Colorate.Horizontal(Colors.green_to_white, "Открытые порты:"))
        for port in open_ports:
            print(Colorate.Horizontal(Colors.green_to_white, f"Порт {port} открыт"))
    else:
        print(Colorate.Horizontal(Colors.green_to_white, "Открытых портов не найдено"))

    input(Colorate.Horizontal(Colors.green_to_white, "\nНажмите Enter для возврата в меню..."))

if __name__ == "__main__":
    target_ip = input(Colorate.Horizontal(Colors.green_to_white, "Введите IP-адрес для сканирования: "))
    port_scan(target_ip)
    clear_console()
    main()