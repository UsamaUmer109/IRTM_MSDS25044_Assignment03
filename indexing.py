import pandas as pd
import json

# Load the lemmatized data
df = pd.read_csv("data/raw/lemmatized_dataset.csv")

print("Building inverted index...")
print(f"Number of documents: {len(df)}")

# Convert string back to list
def string_to_list(text):
    if pd.isna(text) or text == "[]":
        return []
    clean_text = text.strip('[]').replace("'", "")
    tokens = clean_text.split(', ')
    return [t.strip() for t in tokens if t.strip()]

df['Lemmatized_Article'] = df['Lemmatized_Article'].apply(string_to_list)

# Build inverted index
inverted_index = {}

for doc_id, tokens in enumerate(df['Lemmatized_Article']):
    # Count how many times each word appears
    word_count = {}
    for word in tokens:
        word_count[word] = word_count.get(word, 0) + 1
    
    # Add to inverted index
    for word, count in word_count.items():
        if word not in inverted_index:
            inverted_index[word] = {}
        inverted_index[word][doc_id] = count

print(f"Inverted index built with {len(inverted_index)} unique words")

# Show some statistics
print(f"Total documents: {len(df)}")

# Save the inverted index
with open('data/raw/inverted_index.json', 'w') as f:
    json.dump(inverted_index, f)

print("Saved inverted index to data/raw/inverted_index.json")