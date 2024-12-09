from playwright.async_api import async_playwright
import asyncio

async def crawl_website(url, max_depth=1):
    """
    Crawl a website starting from a given URL up to a certain depth.
    Args:
        url (str): The starting URL of the website to crawl.
        max_depth (int): The depth of the crawl (how far to follow links).
    Returns:
        dict: A dictionary containing the crawled pages and their HTML content.
    """
    crawled_data = {}
    visited_urls = set()

    async def crawl(url, depth):
        if depth > max_depth or url in visited_urls:
            return

        visited_urls.add(url)

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            try:
                await page.goto(url, timeout=30000)  # Timeout of 30 seconds
                crawled_data[url] = await page.content()
                links = await page.eval_on_selector_all("a", "elements => elements.map(e => e.href)")
                for link in links:
                    if link.startswith("http"):
                        await crawl(link, depth + 1)
            except Exception as e:
                print(f"Error crawling {url}: {e}")
            finally:
                await browser.close()

    await crawl(url, 0)
    return crawled_data
