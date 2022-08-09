import webbrowser
import http.server

from . import wpages
from . import whandler

class WServer(http.server.HTTPServer):
    def __init__(self, host='localhost', port: int=8080, *args, **kwargs):
        super().__init__(server_address=(host, port), RequestHandlerClass=whandler.whandle(wpages.wmap))
        self.port = port
        self.host = host
 
    def run(self):
        try:
            print('WServer running at:\nhttp://%s:%s' % (self.host, self.port))
            self.serve_forever()
        except KeyboardInterrupt:
            pass
 
        self.server_close()
        print('WServer closed.')

    def show(self):
        webbrowser.open(f'{self.host}:{self.port}')
