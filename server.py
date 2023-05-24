"""
http 服务器
"""
import os
from http.server import HTTPServer, BaseHTTPRequestHandler, ThreadingHTTPServer
import modules as modul


class MyServerHandler(BaseHTTPRequestHandler):
    """http 请求处理"""
    server_version = "MyServer 1.0"

    def do_GET(self):
        """处理GET 请求"""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # 业务数据
        data = modul.get_user_info()

        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes(f"<p>Method:GET {data}</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

    def do_POST(self):
        """处理POST 请求"""
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        self.end_headers()
        # 业务数据
        data = modul.get_user_info()
        self.wfile.write(bytes(data, "utf-8"))
        """
        self.wfile.write(bytes(f"<p>Method:POST {data}</p>", "utf-8"))
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes(f"<p>Method:POST {data}</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
        """

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        self.end_headers()
        self.wfile.write(bytes("Method: HEAD", encoding="utf-8"))

    def do_PUT(self):
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        self.end_headers()
        self.wfile.write(bytes("Method: PUT ", encoding="utf-8"))

    def do_DELETE(self):
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        self.end_headers()
        self.wfile.write(bytes("Method: DELETE ", encoding="utf-8"))

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        self.end_headers()
        self.wfile.write(bytes("Method: OPTIONS ", encoding="utf-8"))


class MixHttpServer(ThreadingHTTPServer):
    """
    我的http server
    可以方便切换运行模型 多线程 、多进程等
    """

    def shutdown_request(self, request):
        super().shutdown_request(request)
        print("my server shutdown_request")

    def handle_timeout(self):
        super().handle_timeout()
        print("my server handle_timeout")

    def handle_error(self, request, client_address):
        super().handle_error(request, client_address)
        print("my server handle_error")


class MyHttpServer:
    """线程服务器"""

    @staticmethod
    def run(host_port: tuple, threaded: bool = False):
        """运行"""
        host, port = host_port
        if threaded:
            web_server = MixHttpServer((host, port), MyServerHandler)
        else:
            web_server = HTTPServer((host, port), MyServerHandler)
        print("Server started http://%s:%s" % (host, port))
        print("Server pid %s" % os.getpid())
        try:
            web_server.serve_forever()
        except (InterruptedError, KeyboardInterrupt):
            web_server.server_close()
            print("exception ! Server stopped")
        finally:
            web_server.server_close()
            print("Server stopped")
