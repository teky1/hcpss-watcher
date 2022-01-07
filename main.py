from discord_webhook import DiscordWebhook
import requests
import time

with open("webhooks.txt") as file:
    whs = file.read().split("\n")

def reportChange():
    for wh in whs:
        webhook = DiscordWebhook(url=wh, content='SOMETHING CHANGED IDK WHAT BCUZ <@!258048636653535234> SUCKS AT CODING **CHECK IT** https://status.hcpss.org')
        response = webhook.execute()

og = requests.get("https://status.hcpss.org").text

while True:
    time.sleep(5)
    new = requests.get("https://status.hcpss.org").text
    print(time.time(), og == new)
    if og != new:
        og = new
        reportChange()

