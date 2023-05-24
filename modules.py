"""
业务逻辑
"""
import json
import time


def get_user_info() -> str:
    """获取用户信息"""
    # ret = 100 // 1
    time.sleep(10)
    data = {
        "name": "name",
        "age": 1
    }
    return json.dumps(data)
