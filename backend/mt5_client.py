import MetaTrader5 as mt5

class MT5Client:
    def __init__(self):
        self.connect()

    def connect(self):
        if not mt5.initialize():
            raise Exception("Error al conectar con MT5")

    def place_order(self, symbol, lot, order_type):
        tick = mt5.symbol_info_tick(symbol)
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot,
            "type": mt5.ORDER_TYPE_BUY if order_type == "BUY" else mt5.ORDER_TYPE_SELL,
            "price": tick.ask if order_type == "BUY" else tick.bid,
            "deviation": 10,
            "magic": 123456,
            "comment": "Orden desde Python",
        }
        return mt5.order_send(request)