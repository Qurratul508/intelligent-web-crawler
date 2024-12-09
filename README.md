# Intelligent Web Crawler

An AI-powered web crawler designed to intelligently scrape, extract, and structure data from multiple websites based on user-defined prompts.

## Features
- Intelligent crawling of website hierarchies and dynamic content.
- Selective data extraction based on user prompts.
- Structured output in JSON, plain text, or CSV formats.
- API support for integration into RAG pipelines.
- Web interface for user-friendly input and data download.

## Getting Started

### Prerequisites
1. Python 3.8+ installed.
2. Git for version control.
3. A virtual environment tool like `venv` or `conda`.

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/intelligent-web-crawler.git
   cd intelligent-web-crawler
   ```
2. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # macOS/Linux
   env\Scripts\activate     # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the initial script to test:
   ```bash
   python main.py
   ```

## Usage

### Basic Crawling
```python
from crawler import Crawler

crawler = Crawler()
data = crawler.scrape(
    url="https://example.com",
    instructions="Extract FAQs and product details",
    depth=2
)
print(data)
```

### API Integration
Run the FastAPI server:
```bash
uvicorn main:app --reload
```
Access the API at `http://127.0.0.1:8000/scrape/`.

### Web Interface
1. Run the server:
   ```bash
   uvicorn main:app --reload
   ```
2. Open `http://127.0.0.1:8000/` in your browser.

## Project Structure
```
intelligent-web-crawler/
├── crawler/                 
│   ├── __init__.py          
│   ├── crawler.py           
│   ├── extractor.py         
│   ├── synthesizer.py       
│   └── utils.py             
├── tests/                   
├── templates/               
├── static/                  
├── main.py                  
├── requirements.txt         
├── README.md                
├── .gitignore               
└── LICENSE                  
```

## Technologies Used
- Python
- Playwright
- BeautifulSoup
- FastAPI
- Uvicorn

## Future Enhancements
- Add support for private website authentication.
- Improve web interface design.
- Enhance prompt understanding with ML models.

## License
This project is licensed under the MIT License.

## Contact
- **Name:** Qurratul Ain Sanjida
- **Email:** sanjidaaaa123@gmail.com
