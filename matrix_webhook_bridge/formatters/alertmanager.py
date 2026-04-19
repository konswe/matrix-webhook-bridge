def format_alertmanager(data: dict) -> list[tuple[str, str]]:
    """Format an Alertmanager webhook payload to a Matrix message."""
    out = []
    external_url = data.get("externalURL", "")
    for a in data.get("alerts", []):
        name = a["labels"].get("alertname", "?")
        severity = a["labels"].get("severity", "").upper()
        summary = a.get("annotations", {}).get("summary", name)
        desc = a.get("annotations", {}).get("description", "")
        starts_at = a.get("startsAt", "")
        fingerprint = a.get("fingerprint", "")
        firing = a["status"] == "firing"
        icon, color = ("🔥", "#e74c3c") if firing else ("✅", "#2ecc71")
        plain = f"{icon} [{severity}] {summary}"
        if starts_at:
            plain += f" (since {starts_at})"
        html = f'<b><font color="{color}">{icon} [{severity}] {summary}</font></b>'
        if desc:
            html += f"<br/><i>{desc}</i>"
        if starts_at:
            html += f"<br/>Since: {starts_at}"
        if fingerprint and external_url:
            html += f'<br/><a href="{external_url}/#/alerts?fingerprint={fingerprint}">View in Alertmanager</a>'
        out.append((plain, html))
    return out
