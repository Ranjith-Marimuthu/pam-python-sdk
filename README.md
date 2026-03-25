# Delinea PAM Python Client

Python script to retrieve a secret password from **Delinea Secret Server** using API token authentication.

## Prerequisites

- Python 3.8+
- Network access to your Secret Server instance
- A valid API token with read access to the target secret

## Setup

```bash
# Clone and enter the repo
cd delinea-python-client

# (Optional) Create a virtual environment
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate  # Linux/macOS

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your actual values
```

## Configuration

| Variable        | Description                                      | Example                                              |
| --------------- | ------------------------------------------------ | ---------------------------------------------------- |
| `TSS_BASE_URL`  | Base URL of your Secret Server instance           | `https://<vault>.<domain>.net/SecretServer`                 |
| `TSS_API_TOKEN` | API Bearer token for authentication               | `ag5...xyz`                                          |
| `SECRET_ID`     | Numeric ID of the secret to retrieve              | `42`                                                 |

## Run

```bash
python src/client.py
```

**Output:**
```
Retrieved password: s3cretP@ss!
```

## How It Works

1. Reads connection details from `.env`
2. Calls `GET /api/v1/secrets/{id}` with `Authorization: Bearer <token>`
3. Finds the item with `slug == "password"` in the response
4. Prints the password value
