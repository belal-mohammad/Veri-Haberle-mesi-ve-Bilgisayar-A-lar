import json
import socket


def add(a, b):
  return a + b


def subtract(a, b):
  return a - b


def multiply(a, b):
  return a * b


def run_operation(item):
  func = item.get("func")
  a = item.get("a")
  b = item.get("b")

  if func == "add":
    return {"func": func, "result": add(a, b)}
  elif func == "subtract":
    return {"func": func, "result": subtract(a, b)}
  elif func == "multiply":
    return {"func": func, "result": multiply(a, b)}
  else:
    return {"func": func, "error": f"Unknown function: {func}"}


ip = "172.16.107.24"
port = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((ip, port))
server.listen(1)
print(f"Server listening on {ip}:{port}...")

conn, addr = server.accept()
print(f"Connected by {addr}")

data = conn.recv(4096)
if data:
  request = json.loads(data.decode("utf-8"))
  results = [run_operation(item) for item in request]
  response = {"results": results}
  conn.sendall(json.dumps(response).encode("utf-8"))

conn.close()
server.close()
