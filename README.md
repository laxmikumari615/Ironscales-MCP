# IRONSCALES MCP Server

A custom Model Context Protocol (MCP) server that integrates
IRONSCALES API with Claude AI.

## Features

- List open IRONSCALES incidents
- Get incident details
- List security awareness campaigns
- Get campaign participants
- Read-only API operations
- Streamable HTTP MCP transport
- Cloud/VPS deployment support

## Architecture

Claude AI
    ↓
MCP Server
    ↓
IRONSCALES API

## Technologies

- Python
- FastMCP / MCP
- IRONSCALES API
- Claude AI
- Ubuntu
- Nginx
- HTTPS / Let's Encrypt

## Configuration

Create a `.env` file:

IRONSCALES_API_KEY=your_api_key
IRONSCALES_COMPANY_ID=your_company_id
IRONSCALES_SCOPE=partner.all

Never commit `.env` or API credentials to GitHub.
