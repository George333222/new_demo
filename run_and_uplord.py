import subprocess
import requests
import json
from datetime import datetime
import sys


xml_file = sys.argv[1] if len(sys.argv) > 1 else "results.xml"


# ================== CONFIGURATION ==================

CLIENT_ID = "A3D52A6110084E1DAE2E8333F1A30A22"
CLIENT_SECRET = "c63f8d508a2921c86822deb9d822347c91e785bcbd9cb2fa341a86a6fa165b04"

PROJECT_KEY = "COM"   # YOUR JIRA PROJECT KEY

AUTH_URL = "https://xray.cloud.getxray.app/api/v2/authenticate"

# IMPORTANT: projectKey MUST be in the URL
IMPORT_URL = f"https://xray.cloud.getxray.app/api/v2/import/execution/junit?projectKey={PROJECT_KEY}"

# ==================================================


def run_tests():
    print("\nRunning Pytest...\n")

    result = subprocess.run([
        "python", "-m", "pytest",
        "--junitxml=results.xml",
        "-v"
    ])

    if result.returncode != 0:
        print("\nSome tests failed. Results will still be uploaded.\n")
    else:
        print("\nTests finished successfully.\n")


def get_xray_token():
    print("Getting Xray authentication token...\n")

    payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(AUTH_URL, json=payload, headers=headers)

    if response.status_code != 200:
        print("Failed to authenticate with Xray")
        print(response.text)
        exit(1)

    token = response.text.replace('"', '')
    print("Token received successfully.\n")
    return token


def upload_results(token):
    print("Uploading results to Xray...\n")

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/xml"
    }

    # IMPORTANT: projectKey must be in URL
    IMPORT_URL = f"https://xray.cloud.getxray.app/api/v2/import/execution/junit?projectKey={PROJECT_KEY}"

    # Read XML as raw text
    with open("results.xml", "rb") as file:
        xml_data = file.read()

    response = requests.post(
        IMPORT_URL,
        headers=headers,
        data=xml_data   # <-- NOT files= , use data=
    )

    print("Xray Response:")
    print("Status Code:", response.status_code)
    print(response.text)

    if response.status_code == 200:
        data = response.json()
        test_exec_key = data.get("testExecIssue", "UNKNOWN")
        print(f"\n SUCCESS! Test Execution created: {test_exec_key}\n")
    else:
        print("\n ERROR uploading results to Xray.\n")



if __name__ == "__main__":
    run_tests()
    token = get_xray_token()
    upload_results(token)
