import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# comment this after first time use
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('averaged_perceptron_tagger')
# --------------------------------------------------------------

def pass_message(message):
    print("preprocessing the message : "+message)
    msg = []

    lemmatizer = WordNetLemmatizer()
    stop_words = stopwords.words('english')

    message = message.lower()  # normalization

    # tockenization
    message_tocken = nltk.word_tokenize(message)
    filter_word = []

    # lemmatization

    for word in message_tocken:
        # x = lemmatizer.lemmatize(word)
        x = word
        msg.append(x)

    # ans = nltk.pos_tag(filter_word)

    # stop word removal
    for word in msg:
        if not word in stop_words:
            filter_word.append(word)
    final_filter = []
    # for word in ans:
    #     val = word[1]
    #     if(val == 'NN' or val == 'NNS' or val == 'NNPS' or val == 'NNP'):
    #         final_filter.append(word[0])

    s = ''
    for word in filter_word:
        s = s + str(word) + ' '

    print(f"After processing: {message}\n\n")
    return s


# --------------------------------------------------------------

if __name__ == '__main__':
    pass_message("Send college notices contact colleges jumping running alpha ? betas0879080")

# --------------------------------------------------------------
