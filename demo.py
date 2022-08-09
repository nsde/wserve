import wserve

@wserve.wpage('/')
def index():
    return 'Hello There'

@wserve.wpage('/hi')
def hi():
    return 'Lorem Ipsum'

server = wserve.WServer(port=1234)
# server.show()
server.run()