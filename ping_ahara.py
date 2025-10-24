import requests, time, hmac, hashlib, os, logging

def ping_ahara():
    url = "https://ahara.v19.tech/api/ping"
    token = os.getenv("AHARA_BEARER_TOKEN")
    signing_secret = os.getenv("AHARA_SIGNING_SECRET")

    if not token or not signing_secret:
        logging.error("Missing required environment variables")
        return

    timestamp = str(int(time.time()))
    signature = hmac.new(signing_secret.encode(), timestamp.encode(), hashlib.sha256).hexdigest()

    headers = {
        "Authorization": f"Bearer {token}",
        "X-Signature": signature,
        "X-Timestamp": timestamp
    }

    try:
        response = requests.get(url, headers=headers, timeout=15)
        logging.info(f"Ahara ping -> {response.status_code}: {response.text}")
        print("Pinged Ahara:", response.status_code)
    except Exception as e:
        logging.error(f"Error pinging Ahara: {e}")

def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    ping_ahara()

if __name__ == "__main__":
    main()
