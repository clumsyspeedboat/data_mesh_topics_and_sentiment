import json

def load_existing_urls(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return set(line.strip() for line in f)
    except FileNotFoundError:
        return set()

def extract_and_update_urls(json_file, output_file):
    # Load existing URLs
    existing_urls = load_existing_urls(output_file)

    # Load the JSON data from the file
    with open(json_file, 'r', encoding='utf-8') as f:
        papers = json.load(f)

    # Extract new URLs
    new_urls = set()
    for paper in papers:
        url = paper.get('url')
        if url and url not in existing_urls:
            new_urls.add(url)

    # Append new URLs to the file
    with open(output_file, 'a', encoding='utf-8') as f:
        for url in new_urls:
            f.write(url + '\n')

    print(f"Added {len(new_urls)} new URLs to '{output_file}'.")
    print(f"Total unique URLs: {len(existing_urls) + len(new_urls)}")

# Run the function
extract_and_update_urls('relevant_papers.json', 'paper_urls.txt')