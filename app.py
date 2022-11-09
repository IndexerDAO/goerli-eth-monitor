import requests
from datetime import datetime
import os
import sys
from dotenv import load_dotenv
load_dotenv()

def get_goerliETH_amount(address):

    url = f"https://goerli.etherscan.io/address/{address}"
    headers = {
        "User-Agent": "My User Agent 1.0"
    }

    now = datetime.now()
    current_time = now.strftime("%m-%d-%Y %H:%M:%S")

    try:
        r = requests.get(url, headers=headers)
        balance = r.text.split('<div class="col-md-8">')[1].split(" Ether")[0].replace("<b>.</b>", ".")
        return {
            "address": address, 
            "balance": round(float(balance), 3),
            "timestamp": current_time
            }
    except Exception as e:
        return e

def create_message_content(goerli_data):
    return {
        "content": f"{goerli_data['address']} \n{goerli_data['balance']} goerliETH remaining"
    }

def post_message(discord_webhook_url, message_content):
    try:
        requests.post(discord_webhook_url, json=message_content)
    except Exception as e:
        return e

def main():
    goerliETH_amount = get_goerliETH_amount(sys.argv[1])
    message = create_message_content(goerliETH_amount)
    post_message(sys.argv[2], message)

if __name__=="__main__":
    main()
