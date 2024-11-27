import requests
import random
import re

# import importlib
# importlib.import_module("main", "../../2024-Oct-30/Group-1" )

def article(suggestion):
    if suggestion[0] in "aeiouAEIOU" or suggestion[0] == "h" and suggestion[1] in "aeiouAEIOU":
        return "an"
    else:
        return "a"

# What are webhooks and why are they useful for us here?
AVATAR_IMAGES = [
    "https://imgs.search.brave.com/K77W9TFiADvZBnQp3qWKrrQOIIQT7mWxlPbBpYXVtZs/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pLmlt/Z2ZsaXAuY29tLzIv/Mm9hamQ4LmpwZw",
    "https://imgs.search.brave.com/IQX78M0Qg_p5C46odIlSkDNQOFCqUzmgm6C2ebVbGk8/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMTU3/NDQxNzk2L3Bob3Rv/L3BvcnRyYWl0LW9m/LWEtcm9ib3QuanBn/P3M9NjEyeDYxMiZ3/PTAmaz0yMCZjPUZf/eDBDLTRobDRCeGpE/RG9ESHFMUks3RTh2/a25YNXFQN0RQVzZ6/Y0FhVmc9",
    "https://imgs.search.brave.com/dFCxE6wYUXn-xfkcw5xPDhyVfSarAc0GQuxT1Nsw4K8/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9pLnBp/bmltZy5jb20vb3Jp/Z2luYWxzLzJlLzkx/L2MxLzJlOTFjMTMw/MWJmMGExZGFmNTAy/MGVkOGQ0ZjhjN2Y2/LmpwZw"
    ]

FULL_WEBHOOK_URL = r"https://discord.com/api/webhooks/1311406830932594858/XLav7UzIkkqCiNmEDXVXQDzdjnQ5rwslnSOvlq6UpdGAZ22k_AmZe9GIGuiznDRJz3cm"
TOKEN = r"XLav7UzIkkqCiNmEDXVXQDzdjnQ5rwslnSOvlq6UpdGAZ22k_AmZe9GIGuiznDRJz3cm"
BOT_NAME = "HarkaNOR the Almighty Demandor"

random_article = requests.get("https://en.wikipedia.org/wiki/Special:Random")
url = random_article.url
thing = re.sub("_", " ", url.split("/")[-1])
# thing = random_article.url.split("/")[-1]
suggestions = [
  "maze builder",
  "web scraper",
  "Game of Life",
  "Twitter clone",
  "Privacy Invader",
  "Anxiety Inducer",
  "Uiua interpreter",
    f"[{thing}]({url})"
]

flavour_message = [
    "I, the Almighty Ruler, command you to build",
    "The hostages will only be freed on the condition that you build",
    "It's my off day, so I'll be nice, just build",
    "The Mission, should you choose to accept it, is to build",
    "You Mere mortals could never understand the complexity it takes to build",
    "Get in the car losers, we're going to build"
]

suggestion = random.choice(suggestions)
message = f"{random.choice(flavour_message)} {article(suggestion)} {suggestion}"

def create_body(message: str):
    return {"username": BOT_NAME, "content": message, "avatar_url": random.choice(AVATAR_IMAGES) } 

response = requests.post(FULL_WEBHOOK_URL, create_body(message))

if not response.ok:
    raise Exception(f"Unsuccessful response: code {response.status_code}")

# response = requests.patch(f"{FULL_WEBHOOK_URL}/messages")
# print("Messages request: ", response.status_code, response )


# https://birdie0.github.io/discord-webhooks-guide/discord_webhook.html
# https://discord.com/developers/docs/resources/webhook
# https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks