from prometheus_client import Counter

requests_total = Counter(
    "bridge_requests_total",
    "Every POST /notify received",
    ["service"],
)

notify_success_total = Counter(
    "bridge_notify_success_total",
    "Matrix send succeeded",
    ["service"],
)

notify_failure_total = Counter(
    "bridge_notify_failure_total",
    "Matrix send failed",
    ["service"],
)

invalid_payload_total = Counter(
    "bridge_invalid_payload_total",
    "400 Bad Request (malformed JSON or oversized)",
    ["service"],
)

auth_failure_total = Counter(
    "bridge_auth_failure_total",
    "401 Unauthorized",
)
