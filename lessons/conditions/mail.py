import time


class mail:
    t = time.time()
    new = False
    list = ["hey there, im a new mail! i was sent 32 minutes ago"]

    @staticmethod
    def get():
        last_mail = mail.list[-1]
        mail.new = False
        return last_mail

    @staticmethod
    def send():
        mail.list.append("hey there, im a new mail! i was sent {}sec ago".format(time.time()-mail.t))
        mail.new = True
