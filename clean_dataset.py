import pandas as pd
import re

def clean_article_text(text):
    """
    Clean text by removing HTML tags and fixing common issues
    """
    if pd.isna(text):
        return ""
    
    text = str(text)
    
    # Remove specific problematic patterns
    text = re.sub(r'</?strong>', ' ', text)  # Remove <strong> and </strong>
    text = re.sub(r'strong>', ' ', text)     # Remove standalone strong>
    text = re.sub(r'</strong', ' ', text)    # Remove incomplete </strong
    text = re.sub(r'/strong', ' ', text)     # Remove /strong prefixes
    
    # Remove other HTML tags 
    text = re.sub(r'<[^>]+>', ' ', text)
    
    # Clean URLs but keep domain names
    text = re.sub(r'https?://', '', text)
    text = re.sub(r'ftp://', '', text)
    
    # Keep only letters, numbers, and basic punctuation
    text = re.sub(r'[^\w\s\.\,\!\?\:\;\(\)\-\'\"\$&\/@]', ' ', text)
    
    # Fix extra whitespace
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    
    return text

def clean_csv_file():
    # Load the CSV file
    df = pd.read_csv("data/raw/Articles.csv", encoding='latin-1')
    
    df['Cleaned_Article'] = df['Article'].apply(clean_article_text)
    
    # Save cleaned data
    output_file = "data/raw/cleaned_articles.csv"
    df.to_csv(output_file, index=False, encoding='utf-8')
    
# Run the cleaning
if __name__ == "__main__":
    clean_csv_file()
    print("Saved dataset with cleaned article column")