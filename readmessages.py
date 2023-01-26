"""
This specific script is for testing purposes!
It was used to test whether an enchant in EPIC RPG was a good one
"""

import json
import sys

import requests

"""
For reading, additional steps need to be taken:
(1) Change authorization code by retrieving it from Discord
    - Enter Developer Tools [Ctrl+Shift+I]
    - Go to [Network Tab]
    - Refresh page [F5] or [Ctrl+R]
    - Find message that says 'messages?limit=50'
    - Scroll through 'Request Headers' and look for 'authorization' key i.e. 'authorization: KEY'
    - Copy and paste the KEY into CHANGE_ME_1
(2) Change channel_id value by retrieving it from Discord
    - Enter Developer Tools [Ctrl+Shift+I]
    - Go to [Network Tab]
    - Enter a message into the channel you want to read from
    - Find message that says 'messages' (should be the most recent one)
    - It should be in the Request URL i.e. 'https://discord.com/api/v9/channels/CHANNEL_ID/messages'
    - Copy CHANNEL_ID to CHANGE_ME_2
IMPORTANT: Do not change to a different channel after starting because it will read from the specific channel
"""

headers = {"authorization": "CHANGE_ME_1"}
channe_id = "CHANGE_ME_2"

checks = ["police_car", "stop there"]
enchant_list = ["OMEGA", "ULTRA-OMEGA", "GODLY", "VOID"]


def read_messages(channelid):
    r = requests.get(
        f"https://discord.com/api/v9/channels/{channelid}/messages", headers=headers
    )
    jsonn = json.loads(r.text)
    print("[+] Reading Messages:\n")
    for idx, value in enumerate(jsonn[:4]):
        print(f"[{idx+1}]", value["author"]["username"], ":", value["content"])
        if any(check in value["content"] for check in checks):
            sys.exit("### GUARD DETECTED ###")
        if value["embeds"]:
            embed = value["embeds"][0]
            if "fields" in embed:
                enchant = embed["fields"][0]["name"]
                if "sparkle" in enchant:
                    enchant = enchant.split("*")[2].upper()
                if enchant in enchant_list:
                    sys.exit(f"### {enchant} ENCHANT DETECTED ###")
        print()


read_messages(channel_id)
