import argparse
from bot.client import BinanceClient
from bot.orders import place_order
from bot.validators import validate_input
from bot.logging_config import setup_logger
import logging

setup_logger()

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:
    validate_input(args.symbol, args.side, args.type, args.quantity, args.price)

    client = BinanceClient().get_client()

    print("\n📌 Placing Order...")
    print("Request:", vars(args))

    response = place_order(
        client,
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    logging.info(f"Request: {vars(args)}")
    logging.info(f"Response: {response}")

    if "error" in response:
        print("\n❌ Failed:", response["error"])
    else:
        print("\n✅ Order placed successfully!")

        print("Order ID:", response.get("orderId", "N/A"))
        print("Status:", response.get("status", "N/A"))

        # Better handling
        executed_qty = response.get("executedQty") or response.get("origQty") or "N/A"
        avg_price = response.get("avgPrice") or "N/A"

        print("Executed Qty:", executed_qty)
        print("Avg Price:", avg_price)

        print("\n🔍 Full Response:")
        print(response)

except Exception as e:
    logging.error(str(e))
    print("\n❌ Error:", str(e))