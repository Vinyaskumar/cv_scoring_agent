import re

def extract_experience(text):
    years = re.findall(r'(\d+)\s+years', text, re.IGNORECASE)
    return max([int(year) for year in years], default=0)

def calculate_score(text):
    score = 0
    keywords = ['machine learning', 'deep learning', 'python', 'neural networks', 'AI', 'data science']
    experience_years = extract_experience(text)

    for keyword in keywords:
        if keyword.lower() in text.lower():
            score += 2

    if experience_years >= 5:
        score += 10
    elif experience_years >= 3:
        score += 6
    else:
        score += 3

    if len(text) > 1000:
        score += 5  # assumes detailed CV

    return min(score, 30)  # max score 30
