import wserve

@wserve.wpage('/', pretty=True) # will use Simple.CSS to style the page a bit
def index():
    return '<h2>Hello There</h2>'

server = wserve.WServer() #
# server.show() # opens the server in your web browser
server.run()