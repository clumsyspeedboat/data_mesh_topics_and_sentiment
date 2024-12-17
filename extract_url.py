import json

# Load the JSON data from the file
with open('relevant_papers.json', 'r', encoding='utf-8') as f:
    papers = json.load(f)

# Use a set to store unique URLs
urls = set()

# Iterate over each paper and extract the URL
for paper in papers:
    url = paper.get('url')
    if url:
        urls.add(url)  # Sets automatically handle duplicates

# Save the URLs to a text file
with open('paper_urls.txt', 'w', encoding='utf-8') as f:
    for url in urls:
        f.write(url + '\n')

print(f"Extracted {len(urls)} unique URLs and saved to 'paper_urls.txt'.")
