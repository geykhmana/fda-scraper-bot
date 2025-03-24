DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/YOUR_WEBHOOK"

# Keywords to look for in FDA PRs
KEYWORDS = ["FDA approval", "Complete Response Letter", "CRL", "PDUFA", "approved", "rejected"]

# Ticker filter — only alert if PR mentions these tickers on these dates
TICKERS = {
    "2025-03-25": ["TLX"],   # Monday
    "2025-03-26": ["THTX"]   # Tuesday
}