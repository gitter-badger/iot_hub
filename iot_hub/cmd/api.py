from iot_hub.common import wsgi

def main():
    server = wsgi.Server()
    server.start(default_port=8080)

if __name__ == '__main__':
    main()
