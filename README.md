# wserve
A simple webserver build from scratch in Python!

```py
import wserve

@wserve.wpage('/') # works like flask!
def index():
    return '<h2>Hello There</h2>'

@wserve.wpage('/hi')
def hi():
    return '<h1>Lorem Ipsum</h1>' # HTML

server = wserve.WServer() #
server.show() # opens the server in your web browser
server.run()
```