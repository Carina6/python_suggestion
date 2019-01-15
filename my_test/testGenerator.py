def consumer():
    r = ''
    while True:
        print('111')
        n = yield r
        print('222')
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    r = c.send(None)
    print(r)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consuming return: %s...' % r)
    c.close()


c = consumer()
produce(c)
