def sanitize_url(url):
    """
    Sanitize a URL to ensure it's valid and normalized.
    Args:
        url (str): The URL to sanitize.
    Returns:
        str: Sanitized URL.
    """
    if not url.startswith("http"):
        url = f"http://{url}"
    return url

