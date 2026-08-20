import json
import os
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TOKEN_FILE = os.path.join(
    BASE_DIR,
    "token.json"
)


def get_saved_token():

    if not os.path.exists(TOKEN_FILE):
        return None

    with open(TOKEN_FILE, "r") as f:
        data = json.load(f)

    generated_time = datetime.fromisoformat(
        data["generated_at"]
    )

    if datetime.now() - generated_time < timedelta(days=7):
        return data["jwt"]

    return None


def save_token(jwt):

    data = {
        "jwt": jwt,
        "generated_at": datetime.now().isoformat()
    }

    with open(TOKEN_FILE, "w") as f:
        json.dump(data, f)