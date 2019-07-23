# # # from random import uniform
# # # from math import sqrt
# # #
# # #
# # # def pi_finder(n, r):
# # #     inside = 0
# # #     for i in range(n):
# # #         x = uniform(-sqrt(r), sqrt(r))
# # #         y = uniform(-sqrt(r), sqrt(r))
# # #         if x**2 + y**2<= r:
# # #             inside += 1
# # #     return inside/n*4
# # #
# # # print(pi_finder(10, 10))
# #
# #
# # args = ['myfile.txt']
# #
# # try:
# #     file = open(*args)
# # except FileNotFoundError:
# #     args.append('w')
# #     file = open(*args)
# #
# # try:
# #     file.write('hello')
# # except Exception as e:
# #     print(e)
# #     file.close()
# #     args.append('a')
# #     file = open(*args)
# #     file.write('\nhello')
# #     file.writelines(['היי',"שלום"])
# # finally:
# #     file.close()
# #
# #
# # # try:
# # #     try:
# # #         try:
# # #             raise Exception('hi')
# # #         except Exception as e:
# # #             raise e
# # #     except Exception as e:
# # #         raise e
# # # except Exception as e:
# # #     print(e)
# # #
# # # import requests
# # #
# # # r = requests.get('10.0.0.61:3001/healthcheck')
# # # if not r.status_code == 200:
# # #     mail.send('fgh@.com')
# def first_recurring(data):
#     result = {}
#     for i in data:
#         if i in result:
#             return i
#         result[i] = 1
#
# s1 = first_recurring('asdfghjkuytrfd')
# s2 = first_recurring('ASDFGTIYUNM<D')
# s3 = first_recurring('987654302368')
# s4 = first_recurring('ABCDABCD')
# s5 = first_recurring('zxcvbnmZXCVBNM1234567')
# assert s1 == 'f'
# assert s2 == 'D'
# assert s3 == '3'
# assert s4 == 'A'
# assert s5 is None




class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name
        self.address = None

    def add_address(self, address):
        self.address = address

    def info(self, address=None):
        if not address:
            if not self.address:
                raise Exception(self.name + ' has missing address, please enter or update the address')
            address = self.address
        print(self.name + ' is ' + str(self.age) + ' years old and lives in ' + address)

p1 = Person('jon', 16)
p2 = Person('dor', 23)
p3 = Person('ran', 18)

p1.add_address('israel ashdod hameyasdim 53')
p1.info()
p2.info()
p3.info('israel ashdod hameyasdim 51')
# print(p1.address)
# print(p2.address)


from exercises.data import get_data

people = get_data(10)















