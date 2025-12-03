# IRTM_MSDS25044_Assignment03
-- =========

OverView:
This project implements a complete Information Retrieval (IR) system that runs locally on your machine. The system processes news articles and provides two search methods:

Boolean Search - Fast exact matching with AND/OR operations

TF-IDF Search - Relevance-based ranking using cosine similarity

-- ===========

Features Implemented: 
1. Boolean Retrieval with Inverted Index  
2. Vector Space Model (TF-IDF + Cosine Similarity)  
3. Binary Independence Model (Probabilistic Ranking)  
4. Relevance Feedback (Rocchio Algorithm)  
5. Comprehensive Text Preprocessing

---------------------------------------
-- Required Libraires:

The issue is that pip is not recognized. This usually happens because:
Python is not properly added to PATH, OR
Virtual environment is not activated, OR

We need to use py -m pip instead

# 1. pandas - for data manipulation
pip install pandas==1.5.3 
py -m pip install pandas==1.5.3
py -m pip install pandas==2.2.3
# 2. numpy - for numerical operations
pip install numpy==1.21.6
py -m pip install numpy==1.21.6
py -m pip install numpy==2.0.2
# 3. scikit-learn - for machine learning and TF-IDF
pip install scikit-learn==1.0.2
py -m pip install scikit-learn==1.0.2
py -m pip install scikit-learn==1.5.1
# 4. nltk - for natural language processing
pip install nltk==3.8.1
py -m pip install nltk==3.8.1
py -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
# 5. tqdm - for progress bars (optional but helpful)
pip install tqdm==4.64.1
py -m pip install tqdm==4.64.1

-- ====================

-> Prepare Dataset
    Download Articles.csv from Kaggle
        Place it in: data/raw/Articles.csv

-- ===========================
How to Run the System

Step 1: Data Cleaning
    bash
        py clean_dataset.py
Cleans HTML tags and fixes encoding issues
Output: data/raw/cleaned_articles.csv
---------------------
Step 2: Tokenization
bash
py tokenization.py
Splits text into individual words
Output: data/raw/tokenized_dataset.csv
----------------------
Step 3: Normalization
bash
py normalization.py
Converts to lowercase and removes stop words
Output: data/raw/normalized_dataset.csv
------------------------
Step 4: Lemmatization
bash
py lemmatization.py
Converts words to their root forms
Output: data/raw/lemmatized_dataset.csv
------------------------
Step 5: Build Index
bash
py indexing.py
Creates inverted index for fast searching
Output: data/raw/inverted_index.json
------------------------------------------
Step 6: Run Searches
Boolean Search
bash
py boolean_search.py
Searches using AND/OR operations
Results saved to data/raw/search_results.txt
TF-IDF Search
bash
py tfidf_search.py
Searches using relevance ranking

Results saved to data/raw/tfidf_results.txt
==============================================