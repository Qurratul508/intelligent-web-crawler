# Intelligent Web Crawler

An AI-powered web crawler designed to intelligently scrape, extract, and structure data from multiple websites based on user-defined prompts.

## Features
- **Dynamic Web Crawling**: Navigate through website hierarchies and handle JavaScript-rendered pages.
- **Selective Data Extraction**: Extract specific types of content (e.g., FAQs, headings, paragraphs) based on user prompts.
- **Depth Control**: Limit how deep the crawler traverses links on a website.
- **Error Handling**: Gracefully handle inaccessible pages, timeouts, and broken links.
- **JSON Output**: Save extracted data in a structured JSON format.
- **API and Web Interface**: Interact with the crawler via a FastAPI-powered web interface.

---

## Getting Started

### Prerequisites
1. **Python**: Version 3.8 or higher.
2. **Git**: For version control.
3. **Playwright**: For dynamic web scraping.
4. **FastAPI**: For the web interface.

### Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Qurratul508/intelligent-web-crawler.git
   cd intelligent-web-crawler
   ```

2. **Create a Virtual Environment**:
   - On macOS/Linux:
     ```bash
     python3 -m venv env
     source env/bin/activate
     ```
   - On Windows:
     ```bash
     python -m venv env
     env\Scripts\activate
     ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   playwright install
   ```

4. **Test the Crawler**:
   ```bash
   python3 main.py
   ```

---

## Usage

### **Basic Crawling**
Run the crawler by modifying `main.py` to include your desired URL, depth, and extraction instructions. For example:
```python
url = "https://sfgov.org"
instructions = "Extract all headings and paragraphs"
crawled_data = await crawl_website(url, max_depth=1)
```

### **Web Interface**
Launch the FastAPI server to interact with the crawler:
```bash
uvicorn web_interface:app --reload
```
1. Open `http://127.0.0.1:8000/docs` in your browser.
2. Use the `/crawl/` endpoint to:
   - Input a URL to crawl.
   - Specify crawl depth.
   - Enter a custom prompt for extraction (e.g., "Extract all headings and FAQs").
3. Download the extracted data as `output.json`.

---

## Project Structure
```
intelligent-web-crawler/
├── crawler/                 
│   ├── __init__.py          # Package initialization
│   ├── crawler.py           # Core crawling logic
│   ├── extractor.py         # Data extraction logic
│   ├── synthesizer.py       # JSON synthesis
│   └── utils.py             # Helper functions
├── tests/                   # Unit tests
├── templates/               # HTML templates for web interface (if any)
├── static/                  # Static files (if any)
├── main.py                  # Entry point for the crawler
├── web_interface.py         # FastAPI web interface
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── LICENSE                  # License file
```

---

## Example Output

### Input:
- **URL**: `https://sfgov.org`
- **Depth**: `1`
- **Prompt**: "Extract headings and paragraphs"

### Output (`output.json`):
```json
{
    "https://sfgov.org": [
        "Welcome to the City and County of San Francisco",
        "City Services",
        "Departments",
        "San Francisco is the cultural, commercial, and financial center of Northern California."
    ]
}
```

---

## How the Crawler Works
1. **Crawling**:
   - The `crawl_website` function traverses links starting from a given URL.
   - It uses Playwright for JavaScript rendering and handles depth control.
2. **Data Extraction**:
   - The `extract_data` function parses HTML with BeautifulSoup to extract headings, paragraphs, or other specified elements.
3. **Data Synthesis**:
   - Extracted content is saved in a structured format (`output.json`).
4. **Error Handling**:
   - Problematic pages (e.g., timeouts) are skipped and logged.

---

## Integration into a RAG Pipeline
1. **Load the JSON Output**:
   - Use the crawled data as a knowledge base for semantic search.
   - Example:
     ```python
     from sentence_transformers import SentenceTransformer
     import json

     with open("output.json") as f:
         data = json.load(f)

     model = SentenceTransformer("all-MiniLM-L6-v2")
     embeddings = [model.encode(content) for content in data.values()]
     ```
2. **RAG Querying**:
   - Combine the embeddings with an AI model (e.g., OpenAI GPT) to enhance context-aware responses.

---

## Challenges
1. **Handling Dynamic Content**:
   - Solved using Playwright for dynamic JavaScript rendering.
2. **Timeouts and Inaccessible Pages**:
   - Implemented error handling to log and skip problematic pages.

---

## Future Enhancements
- Add support for private website authentication.
- Enhance prompt understanding with ML models.
- Improve the web interface for a more user-friendly experience.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact
<<<<<<< HEAD
- **Name**: Qurratul Ain Sanjida
- **Email**: sanjidaaaa123@gmail.com
- **GitHub**: [Qurratul508](https://github.com/Qurratul508)
```

---
=======
- **Name:** Qurratul Ain Sanjida
- **Email:** sanjidaaaa123@gmail.com
>>>>>>> 14510a87be7a8b901fe46ac2c40c9f6098b7e728
