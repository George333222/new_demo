import subprocess
import requests

# ---------------- CONFIG ----------------

CLIENT_ID = "8768DAB1837D41E1B4E928F93F24E63F"
CLIENT_SECRET = "d58197c1ed7b290321324f95bc439857c405b85a0a1a87e6ace32b39c41149b0"

PROJECT_KEY = "COM"

AUTH_URL = "https://xray.cloud.getxray.app/api/v2/authenticate"
IMPORT_URL = f"https://xray.cloud.getxray.app/api/v2/import/execution/junit?projectKey={PROJECT_KEY}"

# ---------------------------------------


def run_tests():
    print("\nRunning Pytest...\n")

    subprocess.run([
        "python", "-m", "pytest",
        "test_automation",
        "--junitxml=results.xml",
        "--html=report.html",
        "--self-contained-html",
        "-v"
    ])


def get_xray_token():
    print("\nGetting Xray authentication token...\n")

    payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }

    r = requests.post(AUTH_URL, json=payload)

    if r.status_code != 200:
        print("Auth failed")
        print(r.text)
        exit(1)

    return r.text.replace('"', '')


def upload_results(token):
    print("\nUploading results to Xray...\n")

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/xml"
    }

    with open("results.xml", "rb") as f:
        xml_data = f.read()

    r = requests.post(
        IMPORT_URL,
        headers=headers,
        data=xml_data
    )

    print("Status:", r.status_code)
    print(r.text)

    if r.status_code == 200:
        data = r.json()
        print("\nTest Execution created:", data.get("testExecIssue"))


if __name__ == "__main__":
    run_tests()
    token = get_xray_token()
    upload_results(token)
