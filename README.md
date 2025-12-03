# ArXiv Search Engine

A **Flask-based web application** that lets you quickly discover research papers from the **arXiv repository**. Perfect for students, researchers, or anyone curious about a specific domain.



## Features

- **Search research papers** by topic or keywords  
- **Filter results** by year  
- **Multi-keyword support** for precise searches  
- **Clean, user-friendly interface**  
- **Pagination** for easy browsing of results  
- **Real-time academic content** fetched using arXiv API (Atom feeds) and Feedparser  



## How It Works

1. **Enter Keywords**:  
   - Type your topic or multiple keywords in the search box.  

2. **Apply Filters (Optional)**:  
   - Use year filters to narrow down results.  

3. **Fetch Papers**:  
   - The app fetches relevant research papers from the arXiv API using Feedparser.  

4. **View Results**:  
   - Results are displayed in a clean interface with pagination for easy navigation.  

5. **Click to Read**:  
   - Each paper links directly to the arXiv page for full access.  



## How to Run

1. **Install Python**  
   - Make sure **Python 3.x** is installed: [python.org](https://www.python.org/downloads/)  

2. **Install Dependencies**  
   - Navigate to the project folder and install required packages:  
     ```bash
     pip install Flask feedparser
     ```  

3. **Download the Project**  
   - Clone the repository:  
     ```bash
     git clone <repository-link>
     ```  

4. **Run the App**  
   - Go to the project folder in your terminal:  
     ```bash
     cd ArXiv_search_engine
     ```  
   - Start the Flask server:  
     ```bash
     python app.py
     ```  

5. **Open in Browser**  
   - Go to:  
     ```
     http://127.0.0.1:5000/
     ```  
   - Enter your search keywords and explore papers.  



## Why This Project

- Learn **Flask web development** with a real-world application  
- Practice **API integration** using the arXiv API and Feedparser  
- Build a **mini research search engine** useful for academics  
- Understand **pagination and dynamic content rendering** in web apps  



## Usage

- Type one or more keywords to search for papers  
- Apply year filters to narrow results (optional)  
- Browse results using pagination  
- Click on a paper title to open it on arXiv  


