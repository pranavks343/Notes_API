import bcrypt


def hash_password(password: str) -> str:
    """Hash a plaintext password with bcrypt. Returns a str safe to store."""
    # bcrypt only considers the first 72 bytes; slice to avoid a ValueError
    # on multibyte passwords that exceed 72 bytes.
    pwd_bytes = password.encode("utf-8")[:72]
    return bcrypt.hashpw(pwd_bytes, bcrypt.gensalt()).decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Check a plaintext password against a stored bcrypt hash."""
    return bcrypt.checkpw(
        plain_password.encode("utf-8")[:72],
        hashed_password.encode("utf-8"),
    )