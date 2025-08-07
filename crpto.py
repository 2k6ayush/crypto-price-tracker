from pycoingecko import CoinGeckoAPI
from twilio.rest import Client

def send_whatsapp_message(body):
    account_sid = 'ACba6d9d036037de51b231148f3531dcdf'
    auth_token = '485f81129126431dbb523b3a379100e4'
    client = Client(account_sid, auth_token)

    from_whatsapp_number = 'whatsapp:+14155238886'
    to_whatsapp_number = 'whatsapp:+9xxxxxxxxxxx'  # Replace with your WhatsApp number

    message = client.messages.create(
        body=body,
        from_=from_whatsapp_number,
        to=to_whatsapp_number
    )
    print(f"WhatsApp message sent: SID {message.sid}")

def price_tracking():
    cg = CoinGeckoAPI()

    # Target prices in INR (Indian Rupee)
    targets = {
        'bitcoin': 8000000,   # 8 million INR
        'ethereum': 250000,   # 2.5 lakh INR
    }

    met_targets = {}

    for crypto, target_price in targets.items():
        response = cg.get_price(ids=crypto, vs_currencies='inr')
        if crypto in response:
            current_price = response[crypto]['inr']
            print(f"Current price of {crypto}: ₹{current_price}")
            if current_price >= target_price:
                met_targets[crypto] = current_price
        else:
            print(f"No price data found for {crypto}")

    if met_targets:
        message_body = "*Target prices met (INR):*\n"
        for crypto, current_price in met_targets.items():
            target_price = targets[crypto]
            message_body += f"- {crypto.capitalize()} reached ₹{current_price} (target ₹{target_price})\n"
        send_whatsapp_message(message_body)
    else:
        print("No target prices met.")

if __name__ == "__main__":
    price_tracking()


