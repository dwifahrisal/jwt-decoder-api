# jwt-decoder

Decode JWT tokens and verify HS256 signatures with zero dependencies — pure Python stdlib.

## Usage

```bash
# decode only
python3 jwt.py eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjMifQ.sig

# decode + verify against a secret
python3 jwt.py <token> my-hmac-secret
```

Handy for debugging tokens on servers where installing packages is not an option.
