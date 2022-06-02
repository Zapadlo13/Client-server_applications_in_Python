"""1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения («Узел доступен», «Узел недоступен»).
При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address()."""

from subprocess import Popen, PIPE
from ipaddress import ip_address


def host_ping(lst_ip: list):
    results = {'Reachable': [], 'Unreachable': []}
    for ip in lst_ip:
        try:
            ip = ip_address(ip)
        except:
            pass

        reply = Popen(f'ping {ip}', shell=False, stdout=PIPE)
        CODE = reply.wait()

        if CODE == 0:
            results.get('Reachable').append(str(ip))
        else:
            results.get('Unreachable').append(str(ip))

    return results


if __name__ == '__main__':
    lst_ip = ['192.168.1.1', 'google.com', 'onliner.by', 'tut.by']
    host_ping(lst_ip)
