def hello(name):
    print('Hello, {}!'.format(name))


# only run if called directly
if __name__ == '__main__':
    name = input('What is your name? ')
    hello(name)

