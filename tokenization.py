import pandas as pd

# Load the cleaned data
df = pd.read_csv("data/raw/cleaned_articles.csv")

print("Starting tokenization...")
print(f"Number of documents: {len(df)}")

# tokenization function
def tokenize_text(text):
    if pd.isna(text):
        return []
    
    # Convert to string and split by spaces
    text_str = str(text)
    tokens = text_str.split()
    
    return tokens

# Apply tokenization 
df['Tokenized_Article'] = df['Cleaned_Article'].apply(tokenize_text)

# Count total tokens
total_tokens = 0
for tokens in df['Tokenized_Article']:
    total_tokens += len(tokens)


print(f"Tokenization completed!")
# Save the tokenized data
df.to_csv("data/raw/tokenized_articles.csv", index=False)
print("\nSaved tokenized Articles")