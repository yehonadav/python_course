def first_recurring(string):
    count = {}
    for char in string:
        if char in count:
            return char
        count[char] = 1


s1 = first_recurring('asdfghjkuytrfd')
s2 = first_recurring('ASDFGTIYUNM<D')
s3 = first_recurring('987654302368')
s4 = first_recurring('ABCDABCD')
s5 = first_recurring('zxcvbnmZXCVBNM1234567')

assert s1 == 'f'
assert s2 == 'D'
assert s3 == '3'
assert s4 == 'A'
assert s5 is None
