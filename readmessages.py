import requests
import json
import sys

checks = ["police_car", "stop there"]
enchant_list = ["OMEGA", "ULTRA-OMEGA", "GODLY", "VOID"]

def read_messages(channelid):
    headers = {
        "authorization": "MzQzNTQwNjk1NTcyNjc2NjA5.Gz4EXf.CKYHtm_5KxcteUXQZ9CJfBLpiArtfvXxbKk2J8"
    }
    r = requests.get(f"https://discord.com/api/v9/channels/{channelid}/messages", headers=headers)
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

read_messages("801300069185749062")