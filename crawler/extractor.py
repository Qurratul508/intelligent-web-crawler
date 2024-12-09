from bs4 import BeautifulSoup

def extract_data(html, instructions):
    """
    Extract specific data from HTML based on user instructions.
    Args:
        html (str): The raw HTML content of a webpage.
        instructions (str): User-defined instructions for data extraction.
    Returns:
        list: A list of extracted data matching the instructions.
    """
    soup = BeautifulSoup(html, "html.parser")

    # Extract headings (h1, h2, h3, etc.)
    headings = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
    heading_texts = [heading.get_text(strip=True) for heading in headings]

    # Extract paragraphs
    paragraphs = soup.find_all("p")
    paragraph_texts = [p.get_text(strip=True) for p in paragraphs]

    # Combine results
    return heading_texts + paragraph_texts
