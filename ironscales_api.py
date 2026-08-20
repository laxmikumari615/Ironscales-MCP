import requests
from token_manager import get_saved_token, save_token
from config import API_KEY, SCOPE


def get_jwt():

    response = requests.post(
        "https://appapi.ironscales.com/appapi/get-token/",
        json={
            "key": API_KEY,
            "scopes": [SCOPE]
        },
        headers={
            "Content-Type": "application/json"
        }
    )

    response.raise_for_status()

    return response.json()["jwt"]


def get_valid_token():

    token = get_saved_token()

    if token:
        print("Using Cached Token")
        return token

    print("Generating New Token")

    jwt = get_jwt()

    save_token(jwt)

    return jwt


def get_open_incidents(company_id):

    jwt = get_valid_token()

    url = f"https://appapi.ironscales.com/appapi/incident/{company_id}/open/"

    response = requests.get(
        url,
        headers={
            "Authorization": f"Bearer {jwt}",
            "Content-Type": "application/json"
        }
    )

    response.raise_for_status()

    return response.json()


def get_recent_incidents(company_id):

    jwt = get_valid_token()

    url = f"https://appapi.ironscales.com/appapi/incident/{company_id}/"

    response = requests.get(
        url,
        headers={
            "Authorization": f"Bearer {jwt}",
            "Content-Type": "application/json"
        }
    )

    response.raise_for_status()

    return response.json()


def get_incident_details(company_id, incident_id):

    jwt = get_valid_token()

    url = f"https://appapi.ironscales.com/appapi/incident/{company_id}/details/{incident_id}"

    response = requests.get(
        url,
        headers={
            "Authorization": f"Bearer {jwt}",
            "Content-Type": "application/json"
        }
    )

    response.raise_for_status()

    return response.json()

def get_campaigns(company_id, period=6):

    jwt = get_valid_token()

    url = (
        f"https://appapi.ironscales.com/appapi/"
        f"campaigns/{company_id}/details?period={period}"
    )

    response = requests.get(
        url,
        headers={
            "Authorization": f"Bearer {jwt}",
            "Content-Type": "application/json"
        }
    )

    response.raise_for_status()

    return response.json()

def get_campaign_participants(company_id, campaign_id):

    jwt = get_valid_token()

    url = (
        f"https://appapi.ironscales.com/appapi/"
        f"campaigns/{company_id}/participants-details"
        f"?campaign_id={campaign_id}"
    )

    response = requests.get(
        url,
        headers={
            "Authorization": f"Bearer {jwt}",
            "Content-Type": "application/json"
        }
    )

    response.raise_for_status()

    return response.json()


def campaign_participant_action(
    company_id,
    campaign_id,
    emails,
    action,
    expiration_date=None
):

    jwt = get_valid_token()

    url = (
        f"https://appapi.ironscales.com/appapi/"
        f"campaigns/{company_id}/participants-actions/"
        f"?campaign_id={campaign_id}"
    )

    payload = {
        "filters": {
            "emails": emails
        },
        "action": action
    }

    if expiration_date:
        payload["expiration_date"] = expiration_date

    response = requests.put(
        url,
        json=payload,
        headers={
            "Authorization": f"Bearer {jwt}",
            "Content-Type": "application/json"
        }
    )

    response.raise_for_status()

    return response.json()