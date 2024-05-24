# Hyperparameters:
* num_top_words: This is the number of top words to extract from each document based on their TF-IDF scores which is 10.
* stop_words='english': Words to ignore during analysis (common words in English that may not contribute meaningful information).
* ngram_range=(1, 4): The range of n-gram sizes to consider. Here, it considers unigrams to four-grams.
* token_pattern=r'\b\w+\b': Regular expression defining what constitutes a "token" or a word, focusing on words bounded by word boundaries.

TF-IDF is employed here to identify and rank the relevance of words in each document within the dataset. This importance is expressed as a numerical score, with higher scores indicating terms that are more relevant to the specific document but less frequent in other documents, thereby helping in highlighting unique aspects of each document.


https://teams.microsoft.com/l/meetup-join/19%3ameeting_MjRiMzZiNmUtZDM2ZS00OTdiLTllYTMtYjczZTI5YTRkOTU0%40thread.v2/0?context=%7b%22Tid%22%3a%2228bcace8-4ce7-4949-868f-170f67122379%22%2c%22Oid%22%3a%22ecb45551-e58c-45eb-ba8d-2e5f875acf2c%22%7d
