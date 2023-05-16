import socket

def main():
    target_host = "0.0.0.0"  # Địa chỉ IP hoặc tên miền của TCP server
    target_port = 9998  # Cổng của TCP server

    # Tạo socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Kết nối tới TCP server
    client.connect((target_host, target_port))

    # Gửi dữ liệu tới server
    message = "Hello, server!"
    client.send(message.encode())

    # Nhận dữ liệu từ server
    response = client.recv(4096)
    print("Received:", response.decode())

    # Đóng kết nối
    client.close()

if __name__ == '__main__':
    main()
