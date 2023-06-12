import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def preprocess_text(text):
    # Remove special characters and digits
    text = re.sub(r"[^a-zA-Z]", " ", text)
    
    # Convert to lowercase
    text = text.lower()
    
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    
    # Join the tokens back into a single string
    preprocessed_text = " ".join(filtered_tokens)
    
    return preprocessed_text

# Example usage
document = "This is an example document for preprocessing!"
preprocessed_document = preprocess_text(document)
print(preprocessed_document)
