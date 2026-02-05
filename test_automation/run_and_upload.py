import subprocess
import requests
import os


XRAY_CLIENT_ID = os.getenv("AE2E52458F244BF1BD861F4A75AF3FEB")
XRAY_CLIENT_SECRET = os.getenv("ba37b9b6e5eed4b4ae00e4eda93b9d1da2cf5fe902039c9b8e40d5d782cd6dbf")

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
