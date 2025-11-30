import pandas as pd
import nltk
from nltk.corpus import stopwords
# Download stopwords
nltk.download('stopwords')

# Load your tokenized data
df = pd.read_csv("data/raw/tokenized_dataset.csv")

print("Starting normalization...")
print(f"Number of documents: {len(df)}")

# Convert string lists to actual lists (same as your tokenization output)
def convert_to_list(token_str):
    if pd.isna(token_str) or token_str == "[]":
        return []
    tokens = token_str.strip('[]').replace("'", "").split(', ')
    return [token.strip() for token in tokens if token.strip()]

df['Tokenized_Article'] = df['Tokenized_Article'].apply(convert_to_list)
df['Tokenized_Heading'] = df['Tokenized_Heading'].apply(convert_to_list)

# Normalization function
def normalize_tokens(tokens):
    if not tokens:
        return []
    
    stop_words = set(stopwords.words('english'))
    normalized_tokens = []
    
    for token in tokens:
        # convert to lowercase
        token_clean = token.lower()
        
        # Remove stop words and short tokens
        if token_clean not in stop_words and len(token_clean) > 2:
            normalized_tokens.append(token_clean)
    
    return normalized_tokens

# Apply normalization to both articles and headings
df['Normalized_Article'] = df['Tokenized_Article'].apply(normalize_tokens)
df['Normalized_Heading'] = df['Tokenized_Heading'].apply(normalize_tokens)

# Count tokens
article_tokens_before = sum(len(tokens) for tokens in df['Tokenized_Article'])
article_tokens_after = sum(len(tokens) for tokens in df['Normalized_Article'])

print(f"Normalization completed!")
print(f"Article tokens - Before: {article_tokens_before}, After: {article_tokens_after}")
print(f"Tokens removed: {article_tokens_before - article_tokens_after}")

# Save normalized data
df.to_csv("data/raw/normalized_dataset.csv", index=False)
print("Saved normalized dataset")