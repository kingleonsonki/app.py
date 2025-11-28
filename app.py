from flask import Flask, render_template, request
import requests

app = Flask(__name__)

SEARCH_API_URL = "https://api.duckduckgo.com/"

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    query = ""
    if request.method == 'POST':
        query = request.form.get('query')
        params = {
            'q': query,
            'format': 'json',
            'no_redirect': 1,
            'no_html': 1
        }
        response = requests.get(SEARCH_API_URL, params=params)
        if response.ok:
            data = response.json()
            results = data.get('RelatedTopics', [])
    return render_template('index.html', results=results, query=query)

if __name__ == '__main__':
    app.run(debug=True)
