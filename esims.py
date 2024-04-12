import json
import requests
import time
import random
import string

WEBHOOK_URL = "https://discord.com/api/webhooks/"

while True:
    char = string.digits
    kar = string.ascii_letters
    n = 4
    m = 16
    s = ''
    l1 = s.join([random.choice(char) for i in range(n)])
    l2 = s.join([random.choice(char) for i in range(n)])
    l3 = s.join([random.choice(kar) for i in range(m)])

    payload = {
  "embeds": [{
    "title": f"070-{l1}-{l2}",
    "image": {
      "url": f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=LPA:1$rakuten.prod.ondemandconnectivity.com${l3}"
    }
  }]
}
    res = requests.post( WEBHOOK_URL, json=payload )

    time.sleep(1)
