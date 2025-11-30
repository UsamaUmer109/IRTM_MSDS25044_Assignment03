import pandas as pd
import nltk

# Download required data for lemmatization
nltk.download('wordnet')

# Load the normalized data
df = pd.read_csv("data/raw/normalized_dataset.csv")

print("Starting lemmatization...")

# Convert string back to list
def string_to_list(text):
    if pd.isna(text) or text == "[]":
        return []
    
    # Remove brackets and quotes, then split
    clean_text = text.strip('[]').replace("'", "")
    tokens = clean_text.split(', ')
    return [t.strip() for t in tokens if t.strip()]

df['Normalized_Article'] = df['Normalized_Article'].apply(string_to_list)

# Initialize lemmatizer
lemmatizer = nltk.stem.WordNetLemmatizer()

def lemmatize_words(word_list):
    if not word_list:
        return []
    
    lemmatized = []
    for word in word_list:
        # Convert to root word
        root_word = lemmatizer.lemmatize(word)
        lemmatized.append(root_word)
    
    return lemmatized

# Apply lemmatization
df['Lemmatized_Article'] = df['Normalized_Article'].apply(lemmatize_words)

print("Lemmatization completed!")

# Save the results
df.to_csv("data/raw/lemmatized_dataset.csv", index=False)
print("Saved lemmatized dataset")