from ironscales_api import (
    get_open_incidents,
    get_incident_details
)
from config import COMPANY_ID
import json

try:

    incidents = get_open_incidents(COMPANY_ID)

    print("OPEN INCIDENTS:")
    print(json.dumps(incidents, indent=4))

    incident_ids = incidents.get("incident_ids", [])

    if incident_ids:

        incident_id = incident_ids[0]

        print(f"\nGetting details for Incident: {incident_id}")

        details = get_incident_details(
            COMPANY_ID,
            incident_id
        )

        print(json.dumps(details, indent=4))

    else:
        print("\nNo Open Incidents Found")

except Exception as e:

    print(e)

    if hasattr(e, "response"):
        print(e.response.text)