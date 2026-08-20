import traceback
import sys

from mcp.server.fastmcp import FastMCP

from ironscales_api import (
    get_open_incidents,
    get_incident_details,
    get_campaigns,
    get_campaign_participants as api_get_campaign_participants
)

from config import COMPANY_ID

mcp = FastMCP("Ironscales MCP")


@mcp.tool()
def list_open_incidents():
    """
    Returns all open incident IDs from Ironscales.
    """
    try:
        return get_open_incidents(COMPANY_ID)

    except Exception as e:
        print("ERROR:", str(e), file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        raise


@mcp.tool()
def get_incident(incident_id: int):
    """
    Returns details for a specific incident.
    """
    try:
        return get_incident_details(
            COMPANY_ID,
            incident_id
        )

    except Exception as e:
        print("ERROR:", str(e), file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        raise


@mcp.tool()
def list_campaigns(period: int = 6):
    """
    Returns campaign list.

    Period:
    0 = Last 24h
    1 = Last 7d
    2 = Last 90d
    3 = Last 180d
    4 = Last 360d
    5 = Current YTD
    6 = All Time
    """
    try:
        return get_campaigns(
            COMPANY_ID,
            period
        )

    except Exception as e:
        print("ERROR:", str(e), file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        raise


@mcp.tool()
def get_campaign_participants(campaign_id: int):
    """
    Returns participant details for a campaign.
    """
    try:
        return api_get_campaign_participants(
            COMPANY_ID,
            campaign_id
        )

    except Exception as e:
        print("ERROR:", str(e), file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        raise


if __name__ == "__main__":
    mcp.run()