import pandas as pd

def try_encodings(file_path):
    encodings = ['latin-1']
    
    for encoding in encodings:
        try:
            df = pd.read_csv(file_path, encoding=encoding)
            return df, encoding
        except Exception as e:
            print(f"{encoding} error: {e}")
            continue
    
# Try to load the dataset
csv_path = "data/raw/Articles.csv"
df, used_encoding = try_encodings(csv_path)

if df is not None:
    print(f" Shape: {df.shape} (rows: {df.shape[0]}, columns: {df.shape[1]})")
    print(f" Columns: {list(df.columns)}")
    
    print("\n FIRST  DOCUMENT:")

    for i in range(min(1, len(df))):
        print(f"\n Document {i+1}:")
        print(f"   Heading: {df.iloc[i]['Heading']}")
        print(f"   Date: {df.iloc[i]['Date']}")
        print(f"   NewsType: {df.iloc[i]['NewsType']}")
        print(f"   Article: {df.iloc[i]['Article']}")
        
    print(f"   Total documents: {len(df)}")
    if 'NewsType' in df.columns:
        news_types = df['NewsType'].value_counts()
        print(f"   News Types Distribution:")
        for news_type, count in news_types.items():
            print(f" -> {news_type}: {count} documents")
else:
    print("\n Could not load the dataset. Please check path and error.")