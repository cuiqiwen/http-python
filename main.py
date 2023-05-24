"""
启动文件
"""
from server import MyHttpServer

if __name__ == "__main__":
    """启动服务"""

    MyHttpServer.run(("localhost", 8080), True)
