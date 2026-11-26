import json
import socket

ip = "172.16.107.24"
port = 5050

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))

request = [
    {"func": "add", "a": 5, "b": 3},
    {"func": "subtract", "a": 5, "b": 3},
    {"func": "multiply", "a": 5, "b": 3},
]

client.sendall(json.dumps(request).encode("utf-8"))

data = client.recv(4096)
response = json.loads(data.decode("utf-8"))

if isinstance(response, dict) and "result" in response:
  print("Sonuç:", response["result"])
else:
  print("Gelen Yanıt:", response)

client.close()
