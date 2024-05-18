import secrets

def generate_secret_key(key_length=32):
    """
    Generates a cryptographically secure random secret key using the secrets module.

    Args:
        key_length (int, optional): The desired length of the secret key in bytes. Defaults to 32 (recommended minimum).

    Returns:
        str: The generated secret key in URL-safe base64 format.
    """

    if key_length < 32:
        raise ValueError("Secret key length must be at least 32 bytes for security reasons.")

    # Use secrets.token_bytes for cryptographically secure random bytes
    random_bytes = secrets.token_bytes(key_length)

    # Encode bytes as URL-safe base64 for easy storage and transmission
    secret_key = random_bytes.hex()

    return secret_key

# # Example usage
# secret_key = generate_secret_key()
# print(secret_key)
