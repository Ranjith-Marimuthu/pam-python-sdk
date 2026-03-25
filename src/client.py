#!/usr/bin/env python3
"""Fetch a secret password from Delinea Secret Server (on-prem) using API token."""

import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("TSS_BASE_URL", "").rstrip("/")
API_TOKEN = os.getenv("TSS_API_TOKEN", "")
SECRET_ID = os.getenv("SECRET_ID", "")


def get_secret_password() -> str:
    """Retrieve the 'password' field from a Secret Server secret."""
    if not all([BASE_URL, API_TOKEN, SECRET_ID]):
        sys.exit("Error: TSS_BASE_URL, TSS_API_TOKEN, and SECRET_ID must be set.")

    url = f"{BASE_URL}/api/v1/secrets/{SECRET_ID}"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}

    resp = requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()

    secret = resp.json()
    for item in secret.get("items", []):
        if item.get("slug") == "password":
            return item["itemValue"]

    sys.exit("Error: No field with slug 'password' found in the secret.")


if __name__ == "__main__":
    password = get_secret_password()
    print(f"Retrieved password: {password}")
