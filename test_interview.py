# https://www.youtube.com/watch?v=fgXCN7A8yzg&t=1953s

# >>>>> https://bitpay.com/api/rates

# Will that work?
d1 = {1: 1}
# d2 = {[1]: 1}
# print(type(([1])))

# What is the difference?
l1 = [i for i in range(10)]
l2 = (i for i in range(10))


def generator():
    for i in range(10):
        yield i


g = generator()
print(type(g))
print(type(generator))

for i in g:
    print(i)

print(dir(g))


# Inherit EmailLogger from Logger
class Logger:
    def log_message(self, msg):
        print('Hello from Logger::log_message')


class EmailLogger(Logger):
    def send_email(self, msg):
        print(f'Sending email ...')

    def log_message(self, msg):
        super().log_message(msg)
        self.send_email(msg)


send_email = EmailLogger()

send_email.log_message('Hello from log_massage')

# What is MRO?

# Create a link between table Student and Group

# Difference between LEFT JOIN and RIGTH JOIN?

# Difference between 'run' and 'start' Docker commands?

# Linux:
#   - how many instances of Django:


