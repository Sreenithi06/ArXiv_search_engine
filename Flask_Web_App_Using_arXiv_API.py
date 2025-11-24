from flask import Flask, request, render_template_string
import feedparser
import math

app = Flask(__name__)

# Function to fetch papers from arXiv
def get_papers(topic, year=None, max_results=50):
    query = '+AND+'.join(topic.split())  # multi-keyword support
    url = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results={max_results}"
    feed = feedparser.parse(url)
    papers = []
    for entry in feed.entries:
        paper_year = int(entry.published[:4])
        if year and paper_year != year:
            continue
        papers.append({
            "title": entry.title,
            "authors": ", ".join(author.name for author in entry.authors),
            "link": entry.link,
            "year": paper_year
        })
    return papers

# Flask route
@app.route("/", methods=["GET", "POST"])
def index():
    papers = None
    topic = ''
    year_input = ''
    page_num = int(request.args.get("page", 1))
    per_page = 10  # papers per page

    if request.method == "POST":
        topic = request.form.get("topic").strip()
        year_input = request.form.get("year").strip()
        year = int(year_input) if year_input.isdigit() else None
        papers = get_papers(topic, year)

    paginated = []
    total_pages = 1
    if papers:
        total_pages = math.ceil(len(papers)/per_page)
        start = (page_num-1)*per_page
        end = start + per_page
        paginated = papers[start:end]

    template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Research Paper Finder</title>
        <style>
            body { font-family: Arial; padding: 20px; }
            h1 { color: #333; }
            input, button { padding: 5px; font-size: 16px; margin-right: 5px; }
            ul { list-style-type: none; padding-left: 0; }
            li { margin-bottom: 10px; }
            a { text-decoration: none; color: blue; }
            .pagination { margin-top: 20px; }
            .pagination a { margin: 0 5px; text-decoration: none; }
        </style>
    </head>
    <body>
        <h1>Research Paper Finder</h1>
        <form method="POST">
            <label>Topic/Keywords:</label>
            <input type="text" name="topic" value="{{topic}}" required>
            <label>Year (optional):</label>
            <input type="text" name="year" value="{{year_input}}" placeholder="e.g., 2023">
            <button type="submit">Search</button>
        </form>

        {% if paginated %}
            <h2>Results (Page {{page_num}}/{{total_pages}}):</h2>
            <ul>
                {% for paper in paginated %}
                    <li>
                        <a href="{{ paper.link }}" target="_blank">{{ paper.title }}</a><br>
                        <em>Authors:</em> {{ paper.authors }} | <em>Year:</em> {{ paper.year }}
                    </li>
                {% endfor %}
            </ul>

            <div class="pagination">
                {% if page_num > 1 %}
                    <a href="/?page={{page_num-1}}">Previous</a>
                {% endif %}
                {% if page_num < total_pages %}
                    <a href="/?page={{page_num+1}}">Next</a>
                {% endif %}
            </div>
        {% elif papers == [] %}
            <p>No papers found for this topic/year.</p>
        {% endif %}
    </body>
    </html>
    """
    return render_template_string(template, paginated=paginated, papers=papers, 
                                  topic=topic, year_input=year_input, page_num=page_num, total_pages=total_pages)

if __name__ == "__main__":
    app.run(port=8000, debug=False, use_reloader=False)
