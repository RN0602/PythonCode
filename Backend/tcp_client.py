import socket


class TCPClient:
  '''TCPクライアント'''
  
  def __init__(self, ip_address, port):
    '''コンストラクタ'''
    self.ip_address = ip_address
    self.port = port
  
  def __del__(self):
    '''デストラクタ'''
    self.socket.close()

  def init_connection(self):
    '''初期設定'''
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.socket.connect((self.ip_address, self.port))

  def send_data(self, data):
    '''データをバイナリで送信'''
    data = str(data).encode()
    self.socket.send(data)

  def receive_data(self):
    '''バイナリデータを受信'''
    data = self.socket.recv(1024)
    return data
