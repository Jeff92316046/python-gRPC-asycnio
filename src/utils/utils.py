import socket

def get_internal_ip():
    """取得本機內網 IP 地址"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

def is_valid_port(port):
    """檢查是否為有效的端口號"""
    return isinstance(port, int) and 0 <= port <= 65535