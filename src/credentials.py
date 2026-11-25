"""Password storage shared by local student and reviewer accounts."""

import re
from hashlib import pbkdf2_hmac
from hmac import compare_digest
from secrets import token_bytes


PASSWORD_ITERATIONS = 600_000
SALT_BYTES = 16
HASH_BYTES = 32


def _hash_password(password, salt):
    return pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, PASSWORD_ITERATIONS, dklen=HASH_BYTES
    )


def normalize_username(username):
    username = username.strip().lower()
    if not re.fullmatch(r"[a-z0-9._-]{1,64}", username):
        raise ValueError("Use 1–64 letters, numbers, dots, underscores, or hyphens for the username.")
    return username


def hash_new_password(password):
    if not 15 <= len(password) <= 128:
        raise ValueError("Use a password with 15–128 characters.")
    salt = token_bytes(SALT_BYTES)
    return salt, _hash_password(password, salt)


def verify_password(password, account):
    if not 15 <= len(password) <= 128:
        return False

    # Perform the same password derivation even for an unknown account.
    salt, expected_hash = account if account else (bytes(SALT_BYTES), bytes(HASH_BYTES))
    matches = compare_digest(_hash_password(password, salt), expected_hash)
    return account is not None and matches
