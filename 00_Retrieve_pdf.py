import requests
import json
import time
import os

# Replace 'your_api_key_here' with your actual API key
API_KEY = ''  # If you have an API key

# Base URL for Semantic Scholar API
BASE_URL = 'https://api.semanticscholar.org/graph/v1/paper/search/bulk'

# Search query and parameters
QUERY = '"data mesh"'  # Use quotes to search for the exact phrase
FIELDS = 'title,abstract,year,authors,venue,url'

# Year range for filtering
START_YEAR = 2019
END_YEAR = 2024

# List to store relevant papers
relevant_papers = []

# Headers
headers = {
    'User-Agent': 'DataMeshSurvey/1.0',
}
if API_KEY:
    headers['x-api-key'] = API_KEY

# Initial parameters
params = {
    'query': QUERY,
    'fields': FIELDS,
    'year': f'{START_YEAR}-{END_YEAR}',
}

# Function to check if a paper is relevant
def is_relevant(paper):
    # Get title and abstract, ensuring they are strings
    title = paper.get('title', '')
    abstract = paper.get('abstract', '')

    if not isinstance(title, str):
        title = ''
    if not isinstance(abstract, str):
        abstract = ''

    combined_text = f"{title} {abstract}".lower()

    # List of terms indicating irrelevant papers (e.g., network mesh structures)
    irrelevant_terms = [
        'network', 'wireless', 'sensor', 'antenna', 'communication',
        'routing', 'protocol', 'mobility', 'channel', 'transmission',
        'vehicular', 'adhoc', 'mesh network', 'wireless mesh'
    ]
    # Exclude papers containing any irrelevant terms
    if any(term in combined_text for term in irrelevant_terms):
        return False

    # List of terms indicating relevant papers
    relevant_terms = [
        'data management', 'data architecture', 'data governance',
        'data engineering', 'data platform', 'data analytics',
        'distributed data', 'domain-driven', 'data mesh'
    ]
    # Include papers containing any relevant terms
    if any(term in combined_text for term in relevant_terms):
        return True

    # Exclude if no relevant terms are found
    return False

# Start retrieving papers
token = None
total_papers = None
retrieved = 0

while True:
    if token:
        params['token'] = token

    response = requests.get(BASE_URL, params=params, headers=headers)
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        print(response.text)
        break

    data = response.json()
    if total_papers is None:
        total_papers = data.get('total', 0)
        print(f"Total papers found: {total_papers}")

    papers = data.get('data', [])
    if not papers:
        break

    for paper in papers:
        if is_relevant(paper):
            relevant_papers.append(paper)
    retrieved += len(papers)
    print(f"Retrieved {retrieved} papers...")

    # Check for continuation token to get next batch of results
    token = data.get('token')
    if not token:
        break

    # Respect rate limits by pausing between requests
    time.sleep(1)

print(f"Total relevant papers found: {len(relevant_papers)}")

def load_existing_papers(filename):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

# Function to check if a paper is already in the list
def paper_exists(paper, existing_papers):
    return any(
        existing['title'] == paper['title'] and
        existing['year'] == paper['year'] and
        existing['url'] == paper['url']
        for existing in existing_papers
    )

# Load existing papers
filename = 'relevant_papers.json'
existing_papers = load_existing_papers(filename)

# Merge new papers with existing papers
new_papers = []
for paper in relevant_papers:
    if not paper_exists(paper, existing_papers):
        new_papers.append(paper)

# Append new papers to existing papers
updated_papers = existing_papers + new_papers

print(f"Existing papers: {len(existing_papers)}")
print(f"New papers added: {len(new_papers)}")
print(f"Total papers after update: {len(updated_papers)}")

# Save the updated results to the file
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(updated_papers, f, ensure_ascii=False, indent=2)

print(f"Updated papers saved to {filename}")
    

