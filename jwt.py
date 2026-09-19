#!/usr/bin/env python3
"""Decode a JWT and optionally verify its HS256 signature — stdlib only."""

import base64
import hashlib
import hmac
import json
import sys


def b64decode_part(part: str) -> bytes:
    padding = "=" * (-len(part) % 4)
    return base64.urlsafe_b64decode(part + padding)


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: python3 jwt.py <token> [hmac-secret]", file=sys.stderr)
        return 1

    parts = sys.argv[1].split(".")
    if len(parts) != 3:
        print("invalid JWT: expected three dot-separated parts", file=sys.stderr)
        return 1

    header = json.loads(b64decode_part(parts[0]))
    payload = json.loads(b64decode_part(parts[1]))

    print("=== header ===")
    print(json.dumps(header, indent=2))
    print("=== payload ===")
    print(json.dumps(payload, indent=2))

    if len(sys.argv) > 2:
        key = sys.argv[2].encode()
        sig = hmac.new(key, f"{parts[0]}.{parts[1]}".encode(), hashlib.sha256).digest()
        expected = base64.urlsafe_b64encode(sig).rstrip(b"=").decode()
        print("=== signature ===")
        print("valid" if expected == parts[2] else "INVALID")
    return 0


if __name__ == "__main__":
    sys.exit(main())
