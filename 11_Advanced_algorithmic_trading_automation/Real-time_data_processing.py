import websocket
import json
import ssl

def on_message(ws, message):
    data = json.loads(message)
    print("Receiving data:", data)

def on_error(ws, error):
    print("Error:", error)

def on_close(ws, close_status_code, close_msg):
    print("Connection closed:")

def on_open(ws):
    print("Connection opened:")

ws_url = "wss://stream.binance.com:9443/ws/btcusdt@trade"

ws = websocket.WebSocketApp(
    ws_url,
    on_open=on_open,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close
)


# Run WebSocket with SSL verification turned off
ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
