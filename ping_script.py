import requests
import logging
import os

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def ping_endpoints():
    endpoints = [
        {
            "url": "https://daunrodo.onrender.com/",
            "use_bearer": False
        },
        {
            "url": "https://ahara.v19.tech/api/ping", 
            "use_bearer": True
        }
    ]

    bearer_token = os.getenv("AHARA_BEARER_TOKEN")

    for item in endpoints:
        url = item["url"]
        headers = {}

        if item["use_bearer"]:
            if not bearer_token:
                logging.error("Bearer token not set for Ahara.")
                continue
            headers["Authorization"] = f"Bearer {bearer_token}"

        try:
            response = requests.get(url, headers=headers, timeout=10)
            logging.info(f"Pinged {url} | Status: {response.status_code}")
            print(f"Pinged {url} -> {response.status_code}")
        except Exception as e:
            logging.error(f"Error pinging {url}: {e}")

def main():
    logging.info("Starting scheduled ping...")
    ping_endpoints()
    logging.info("Finished all pings.")

if __name__ == "__main__":
    main()
