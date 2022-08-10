import wserve

builder = wserve.WBuilder()

builder.add('h5', 'This can be displayed at the top of various subpages.', before=True, style={'color': 'green'})
builder.add('h5', 'This can be displayed at the bottom of various subpages.', after=True, style={'color': 'teal'})

@wserve.wpage('/', pretty=True)
def home():
    title = builder.add('h1', 'This is the homepage', style={'color': 'lightblue'})
    link = builder.add('a', 'Click here to open /hello', href='/hello')
    return builder.build(title, link)

@wserve.wpage('/hello', pretty=True)
def hello():
    return builder.build(builder.add('h1', 'Hello there!', style={'color': 'pink'}), builder.add('a', 'Return home', href='/'))

server = wserve.WServer() #
# server.show() # opens the server in your web browser
server.run()