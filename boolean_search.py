import json
import pandas as pd

# Load the index and data
with open('data/raw/inverted_index.json', 'r') as f:
    index = json.load(f)

data = pd.read_csv("data/raw/lemmatized_dataset.csv")

def search_boolean(query, operation="AND"):
    """
    Search documents using boolean AND or OR
    """
    words = query.lower().split()
    
    if not words:
        return []
    
    # Get document sets for each word
    doc_sets = []
    for word in words:
        if word in index:
            # Convert string keys to integers
            doc_ids = set(int(doc_id) for doc_id in index[word].keys())
            doc_sets.append(doc_ids)
        else:
            doc_sets.append(set())
    
    # Apply boolean operation
    if operation == "AND":
        result = set.intersection(*doc_sets) if doc_sets else set()
    elif operation == "OR":
        result = set.union(*doc_sets) if doc_sets else set()
    else:
        result = set()
    
    return list(result)

# Example usage and save results
if __name__ == "__main__":
    # Test a search
    query = "imran khan"
    results = search_boolean(query, "AND")
    
    print(f"Search query: {query}")
    print(f"Found {len(results)} documents")
    
    # Save results to file
    with open('data/raw/search_results.txt', 'w') as f:
        f.write(f"Query: {query}\n")
        f.write(f"Operation: AND\n")
        f.write(f"Found {len(results)} documents\n")
        f.write(f"Document IDs: {results}\n\n")
        
        #  document details
        f.write("Document details:\n")
        count = 0
        for doc_id in results:
            if count >= len(results):
                break
            heading = data['Heading'].iloc[doc_id]
            f.write(f"ID {doc_id}: Heading {heading}\n")
            count += 1
    
    print("Results saved to search_results.txt")