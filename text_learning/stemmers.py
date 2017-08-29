import nltk
nltk.download()
from nltk.corpus import stopwords
sw = stopwords.words("english")

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
print stemmer.stem("responsiveness")
print stemmer.stem("response")
print stemmer.stem("unresponsive")
print stemmer.stem("responsivity")

from nltk.stem.wordnet import WordNetLemmatizer
stemmer = WordNetLemmatizer()
print stemmer.lemmatize("responsiveness")
print stemmer.lemmatize("response")
print stemmer.lemmatize("unresponsive")
print stemmer.lemmatize("responsivity")

from nltk.stem import RegexpStemmer
stemmer = RegexpStemmer('ing$|s$|e$|able$', min=4)
print stemmer.stem("responsiveness")
print stemmer.stem("response")
print stemmer.stem("unresponsive")
print stemmer.stem("responsivity")

from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
print stemmer.stem("responsiveness")
print stemmer.stem("response")
print stemmer.stem("unresponsive")
print stemmer.stem("responsivity")