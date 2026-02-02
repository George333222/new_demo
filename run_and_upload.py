import subprocess
import requests
import os

XRAY_CLIENT_ID = os.getenv("A3D52A6110084E1DAE2E8333F1A30A22")
XRAY_CLIENT_SECRET = os.getenv("c63f8d508a2921c86822deb9d822347c91e785bcbd9cb2fa341a86a6fa165b04")

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

    token = r.json()

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/xml"
    }

    with open("results.xml", "rb") as f:
        requests.post(
            "https://xray.cloud.getxray.app/api/v2/import/execution/junit",
            headers=headers,
            data=f
        )

if __name__ == "__main__":
    run_tests()
    upload_to_xray()
