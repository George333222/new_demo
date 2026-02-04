import subprocess
import requests
import os

XRAY_CLIENT_ID = os.getenv("B3BBCBCC5CAB404994ED64D5A40B6A5C")
XRAY_CLIENT_SECRET = os.getenv("5007d06bbde25745f9a32513528e27b7ec689019722e678cd0588be2e318006d")

def run_tests():
    subprocess.run(
        ["pytest", "-m", "smoke", "--junitxml=results.xml"],
        check=True
    )

def upload_to_xray():
    auth_url = "https://xray.cloud.getxray.app/api/v2/authenticate"

    r = requests.post(auth_url, json={
        "client_id": XRAY_CLIENT_ID,
        "client_secret": XRAY_CLIENT_SECRET
    })

    token = r.text

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/xml"
    }

    with open("smoke.xml", "rb") as f:
        requests.post(
            "https://xray.cloud.getxray.app/api/v2/import/execution/junit",
            headers=headers,
            data=f
        )

if __name__ == "__main__":
    run_tests()
    upload_to_xray()
