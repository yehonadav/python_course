def check_ip_byte(dl,i,chars_left,ip, dot='exist'):
    index, result = i + 1, 'fail'
    if len(dl) - (i) >= chars_left:
        n = dl[i]
        if n.isdigit():
            i += 1
            while n.isdigit():
                if i < len(dl):
                    if dl[i].isdigit():
                        n += dl[i]
                        i += 1
                    else:
                        i -= 1
                        break
                else:
                    i -= 1
                    break
            index = i + 1
            if int(n) > 255:
                return result, index, ip
            elif len(n) > 3:
                return result, index, ip
            elif dot == 'skip':
                ip += n
                return 'ok', index, ip
            elif index < len(dl):
                if dl[index] == '.':
                    ip += n + '.'
                    index += 1
                    return 'ok', index, ip
    return result, index, ip


def ip_lookup(data_line):
    if len(data_line) > 6:
        i = 0
        while i < len(data_line):
            ip = ''
            for c in [7,5,3]:
                result, i, ip = check_ip_byte(data_line, i, c, ip)
                if result != 'ok':
                    break
            if result == 'ok':
                result, i, ip = check_ip_byte(data_line, i, 1, ip, dot='skip')
                if result == 'ok':
                    ip = ip.split('.')
                    for i in range(len(ip)):
                        while len(ip[i]) > 1:
                            if ip[i].startswith('0'):
                                ip[i] = ip[i][1:]
                            else:
                                break
                    return 'ip found: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3])
        return 'ip not found'
    else:
        return 'ip not found'


if '__main__' == __name__:
    # test the function
    print(ip_lookup('ffff 00.30.1.4441 and stay home'))
    print(ip_lookup('ffff 0000.30.1.41 and stay home'))
    print(ip_lookup('ffff 300.30.1.44 and stay home'))
    print(ip_lookup('0000.300.0001.4441 and stay home'))
    print(ip_lookup('080.30.1.4441'))
    print(ip_lookup('00.3y0.1.1'))
    print(ip_lookup('00.30.1.44d41'))
    print(ip_lookup('00.30.1.4441'))
    print(ip_lookup('00.30.1.'))
    print(ip_lookup('00630616441'))
    print(ip_lookup('0.0.0.0'))
    print(ip_lookup('67.78.11.24/30'))
    print(ip_lookup('192.168.0.1'))