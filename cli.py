import argparse
from bot.orders import place_order
from bot.validators import validate_inputs
from bot.logging_config import setup_logging

setup_logging()

parser = argparse.ArgumentParser(description="Trading Bot")

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True)
parser.add_argument("--price", required=False)

args = parser.parse_args()

try:
    symbol, side, order_type = validate_inputs(
        args.symbol, args.side, args.type, args.quantity, args.price
    )

    print("\n📊 Order Summary")
    print(f"Symbol: {symbol}")
    print(f"Side: {side}")
    print(f"Type: {order_type}")
    print(f"Quantity: {args.quantity}")
    if args.price:
        print(f"Price: {args.price}")

    order = place_order(symbol, side, order_type, args.quantity, args.price)

    if order:
        print("\n✅ Order Successful")
        print(f"Order ID: {order.get('orderId')}")
        print(f"Status: {order.get('status')}")
        print(f"Executed Qty: {order.get('executedQty')}")
        print(f"Avg Price: {order.get('avgPrice', 'N/A')}")
    else:
        print("\n❌ Order Failed")

except Exception as e:
    print(f"\n⚠️ Error: {e}")