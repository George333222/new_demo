import subprocess
import requests
import json
import os

# =========================
# CONFIG (PUT YOUR VALUES)
# =========================

CLIENT_ID = "B3BBCBCC5CAB404994ED64D5A40B6A5C"
CLIENT_SECRET = "5007d06bbde25745f9a32513528e27b7ec689019722e678cd0588be2e318006d"

XRAY_AUTH_URL = "https://xray.cloud.getxray.app/api/v2/authenticate"
XRAY_IMPORT_URL = "https://xray.cloud.getxray.app/api/v2/import/execution/junit"

RESULTS_FILE = "results.xml"


# =========================
# RUN PYTEST
# =========================

def run_tests():
    print("\nRunning pytest...\n")
    subprocess.run(["python", "-m", "pytest", "--junitxml=results.xml"])
    print("\nTests finished successfully.\n")


# =========================
# GET XRAY TOKEN
# =========================

def get_xray_token():
    print("Authenticating with Xray...")

    payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(XRAY_AUTH_URL, headers=headers, data=json.dumps(payload))

    if response.status_code != 200:
        print("Authentication failed!")
        print(response.text)
        return None

    token = response.text.replace('"', '')
    print("Authentication successful.\n")
    return token


# =========================
# UPLOAD RESULTS
# =========================

def upload_results():
    token = get_xray_token()
    if not token:
        print("Cannot upload results without token.")
        return

    print("Uploading results to Xray...\n")

    headers = {
        "Authorization": f"Bearer {token}"
    }

    with open(RESULTS_FILE, "rb") as f:
        response = requests.post(XRAY_IMPORT_URL, headers=headers, files={"file": f})

    print("Xray Response:")
    print("Status Code:", response.status_code)
    print(response.text)

    if response.status_code == 200:
        print("\n Results uploaded successfully to Xray!")
    else:
        print("\n Error uploading results to Xray.")


# =========================
# MAIN
# =========================

if __name__ == "__main__":
    run_tests()
    upload_results()
