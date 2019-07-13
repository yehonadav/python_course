class FindIPv4:
    def __init__(self, string):
        self.data = string
        self.results = []
        self.i = 0
        if len(string) < 7:
            self.find_one = lambda: None
            self.find_all = lambda: None

    def show(self):
        if len(self.results) == 0:
            print('ip not found')
        elif len(self.results) == 1:
            print(f'ip address found: {self.results[0]}')
        else:
            print('found ip addresses:')
            for ip in self.results:
                print(f'    {ip}')

    def get(self):
        return self.results

    def _check_ip_byte(self, i, chars_left, ip, dot='exist'):
        string = self.data
        index, result = i + 1, 'fail'
        if len(string) - i >= chars_left:
            n = string[i]
            if n.isdigit():
                i += 1
                while n.isdigit():
                    if i < len(string):
                        if string[i].isdigit():
                            n += string[i]
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
                    if len(string) > index:
                        if string[index] == '/':
                            index += 1
                            if len(string) > index:
                                if string[index].isdigit():
                                    index += 1
                                    if len(string) > index:
                                        if string[index].isdigit():
                                            index += 1
                                        elif string[index] in (' ', '\n', '\t'):
                                            pass
                                        else:
                                            while len(string) > index:
                                                if string[index] in (' ', '\n', '\t'):
                                                    break
                                                index += 1
                                            return 'fail', index, ip
                                else:
                                    while len(string) > index:
                                        if string[index] in (' ', '\n', '\t'):
                                            break
                                        index += 1
                                    return 'fail', index, ip
                        if string[index] not in (' ', '\n', '\t'):
                            while len(string) > index:
                                if string[index] in (' ', '\n', '\t'):
                                    break
                                index += 1
                            return 'fail', index, ip
                    ip += n
                    return 'ok', index, ip
                elif index < len(string):
                    if string[index] == '.':
                        ip += n + '.'
                        index += 1
                        return 'ok', index, ip
        return result, index, ip

    def find_one(self):
        string = self.data
        i = self.i
        while i < len(string):
            while i < len(string):
                if string[i].isdigit():
                    if i > 0:
                        if string[i-1] in (' ', '\n', '\t'):
                            break
                    else:
                        break
                i += 1
            ip = ''
            for c in [7, 5, 3]:
                result, i, ip = self._check_ip_byte(i, c, ip)
                if result != 'ok':
                    break
            else:
                result, i, ip = self._check_ip_byte(i, 1, ip, dot='skip')
                if result == 'ok':
                    ip = ip.split('.')
                    for b in range(len(ip)):
                        while len(ip[b]) > 1:
                            if ip[b].startswith('0'):
                                ip[b] = ip[b][1:]
                            else:
                                break
                    self.results.append(f'{ip[0]}.{ip[1]}.{ip[2]}.{ip[3]}')
                    break
        self.i = i
        return self

    def find_all(self):
        while len(self.data) - self.i > 6:
            self.find_one()
            self.i += 1
        return self


if '__main__' == __name__:
    # test the function
    data = [
        'ffff 00.30.1.4441 and stay home',
        'ffff 0000.30.1.41 and stay home',
        'ffff 300.30.1.44 and stay home',
        '0000.300.0001.4441 and stay home',
        '080.30.1.4441',
        '00.3y0.1.1',
        '0.1.100.30.5',
        '00.30.1.44d41',
        '00.30.1.4441',
        '00.30.1.',
        '00630616441',
        '0.0.0.0',
        '67.78.11.24/30',
        '192.168.0.1'
    ]
    ip_lookup = FindIPv4('\n'.join(data))
    ip_lookup.find_all().show()
