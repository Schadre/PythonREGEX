import re 

def analyze_sentiment(comment):
    positive_pattern = r"\b(thank|love|happy|great|excellent|good)\b"
    negative_pattern = r"\b(hate|angry|bad|terrible|poor|worst)\b"

    try:
        if re.search(positive_pattern, comment, re.IGNORECASE):
            return "Positive"
        elif re.search(negative_pattern, comment, re.IGNORECASE):
            return "Negative"
        else:
            return "Neutral"
    except Exception as e:
        print(f"Error analyzing comment: {e}")
        return "Neutral"

comments = [
    "I love this product!",
    "Terrible service, I'm angry.",
    "Not sure about the quality.",
    "Excellent customer support, thank you!",
    "Worst experience ever."
]

sentiment_count = {"Positive": 0, "Negative": 0, "Neutral": 0}
for comment in comments:
    sentiment = analyze_sentiment(comment)
    sentiment_count[sentiment] += 1

for sentiment, count in sentiment_count.items():
    print(f"{sentiment} Comments: {count}")