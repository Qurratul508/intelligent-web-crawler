import asyncio
from crawler.crawler import crawl_website
from crawler.extractor import extract_data
from crawler.synthesizer import synthesize_data

async def main():
    # Define the target website and instructions
    url = "https://sfgov.org"  # San Francisco Government website
    instructions = "Extract all headings and paragraphs"

    # Crawl the website up to a certain depth
    print(f"Crawling website: {url}")
    crawled_data = await crawl_website(url, max_depth=1)

    # Extract relevant data based on instructions
    print(f"Extracting data from crawled pages...")
    extracted_data = {}
    for page_url, html in crawled_data.items():
        extracted_data[page_url] = extract_data(html, instructions)

    # Save the extracted data
    print("Saving extracted data...")
    synthesize_data(extracted_data, output_file="output.json")
    print("Data successfully saved to output.json")

if __name__ == "__main__":
    asyncio.run(main())
