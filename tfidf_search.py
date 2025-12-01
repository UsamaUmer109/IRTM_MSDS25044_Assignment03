import json
import pandas as pd
import math

# Load index and data
with open('data/raw/inverted_index.json', 'r') as f:
    index = json.load(f)

data = pd.read_csv("data/raw/lemmatized_dataset.csv")

# Total documents
N = len(data)

# Calculate IDF
idf = {}
for word, docs in index.items():
    df = len(docs)
    idf[word] = math.log(N / (df + 1)) + 1

# Create TF-IDF vectors
vectors = {}
for doc_id in range(N):
    vectors[doc_id] = {}

for word, docs in index.items():
    for doc_str, freq in docs.items():
        doc_id = int(doc_str)
        tfidf = freq * idf[word]
        vectors[doc_id][word] = tfidf

# Search function
def search(query, top=10):
    query_words = query.lower().split()
    
    query_vec = {}
    for word in query_words:
        if word in idf:
            query_vec[word] = idf[word]
    
    if not query_vec:
        return []
    
    results = []
    for doc_id in range(N):
        doc_vec = vectors[doc_id]
        dot = 0
        q_len = 0
        d_len = 0
        
        for word, q_weight in query_vec.items():
            q_len += q_weight * q_weight
            if word in doc_vec:
                d_weight = doc_vec[word]
                dot += q_weight * d_weight
                d_len += d_weight * d_weight
        
        if q_len > 0 and d_len > 0:
            sim = dot / (math.sqrt(q_len) * math.sqrt(d_len))
            results.append((doc_id, sim))
    results.sort(key=lambda x: x[1], reverse=True)
    return results[:top]

# Run and save results
if __name__ == "__main__":
    query = "imran khan"
    results = search(query, 5)
    # Save to file
    with open('data/raw/tfidf_results.txt', 'w') as f:
        f.write(f"TF-IDF Search Results\n")
        f.write(f"Query: {query}\n\n")
        for doc_id, score in results:
            heading = data['Heading'].iloc[doc_id]
            article = data['Cleaned_Article'].iloc[doc_id]
            
            f.write(f"Document {doc_id}\n")
            f.write(f"Score: {score:.4f}\n")
            f.write(f"Heading: {heading}\n")
            f.write(f"Article: {article}\n\n")
    
    print("Results saved to tfidf_results.txt")