"""2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона.
Меняться должен только последний октет каждого адреса. По результатам проверки должно выводиться соответствующее сообщение."""
import ipaddress

from task_1 import host_ping


def get_list_ip_address(start_ip, count_ip):
    lst_ip = start_ip.split('.')
    return ['.'.join(lst_ip[:3]) + '.' + str(int(lst_ip[3]) + n) for n in range(count_ip)]


def host_range_ping():
    print('Пример: 192.168.1.1')
    start_ip = input('Введите начальный ip адрес:')
    try:
        ipaddress.ip_address(start_ip)
    except:
        print('Введен некорректный ip адрес!')
        return

    count_ip = int(input('Сколько адресов проверять?: '))

    if int(start_ip.split('.')[3]) + count_ip > 254:
        print('Превышено максимальное количество хостов!')
        return

    lst_ip = get_list_ip_address(start_ip, count_ip)
    results = host_ping(lst_ip)

    return results


#  ba = subnet.broadcast_address
#   print(ba)
#  print(list(subnet.hosts()))


if __name__ == '__main__':
    host_range_ping()
