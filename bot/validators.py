def validate_inputs(symbol, side, order_type, quantity, price):
    symbol = symbol.upper()
    side = side.upper()
    order_type = order_type.upper()

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")

    if float(quantity) <= 0:
        raise ValueError("Quantity must be positive")

    if order_type == "LIMIT":
        if price is None or float(price) <= 0:
            raise ValueError("Valid price required for LIMIT order")

    return symbol, side, order_type