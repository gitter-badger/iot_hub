from eventlet import wsgi
import eventlet

def parse_request(environ):
    response = ""
    method = environ.get('REQUEST_METHOD')
    if method == 'GET':
        response = "GET"
    elif method == 'POST':
        response = "POST"

    return response + "\n"

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    
    return parse_request(environ)

if __name__ == '__main__':
    bind_address = '0.0.0.0'
    port = 8080
    server_socket = eventlet.listen((bind_address, port))

    wsgi.server(server_socket, application)
