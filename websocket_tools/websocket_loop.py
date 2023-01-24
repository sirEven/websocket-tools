import websocket

class WebsocketLoop:
    def __init__(
        self,
        bot_id: str,
        socket_host,
        on_open,
        on_message,
        on_error,
        on_close,
    ):
        self.bot_id = bot_id
        self.socket_host = socket_host
        self.on_open = on_open
        self.on_message = on_message
        self.on_error = on_error
        self.on_close = on_close
        self.ws = None

    def run(self):
        socket_host = self.socket_host
        self.ws = websocket.WebSocketApp(
            socket_host,
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        self.ws.run_forever()

    def terminate(self):
        self.ws.close()