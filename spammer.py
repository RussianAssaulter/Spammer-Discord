import httpx, json, time, threading, random, os






if not os.path.exists("tokens.txt"):
    with open("tokens.txt", "w") as f:
        f.write("")


with open("tokens.txt", "r") as f:
    tokens = f.read().splitlines()




def send_req(channel, message, amount):
    while True:
        url = f"https://discord.com/api/v9/channels/{channel}/messages"
        hdrs = {
            "Authorization": random.choice(tokens),
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML," " like Gecko) Chrome/92.0.4515.159 Safari/537.36",
            "Accept-Language": "en-US",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Accept": "*/*",
            "Referer": "https://discord.com/channels/" + channel,
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "TE": "trailers"
        }
        payload = {"content": message}
        for _ in range(len(amount)):
            try:
                r = httpx.post(url, headers=hdrs, data=json.dumps(payload))
                if r.status_code == 200:
                    print(f"[✅] 200 | Sent Message")
                elif r.status_code == 429:
                    print(f"[⚠️] 429 | Rate Limited")
            except Exception as e:
                print(f"[-] Error: {e}")
                pass
        time.sleep(0.1)





def main_spam():
    channel = input("Channel ID: ")
    message = input("Message: ")
    amount = input("Amount: ")
    for t in tokens:
        thr = threading.Thread(target=send_req, args=(channel, message, amount))
        thr.start()



if __name__ == "__main__":
    main_spam()
        
            

