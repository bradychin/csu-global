import random

users = ['Ryan', 'Jessica', 'Hope', 'Albert', 'Jackson']
content = {
    'sports': ['Hockey', 'Formula 1', 'Football'],
    'tech': ['AI Trends', 'Generative AI', 'Machine Learning'],
    'food': ['Healthy Recipies', 'Christmas Snacks', 'Local Restaurants']
}

content_preferences = {}
for user in users:
    content_preferences[user] = random.choice(list(content.keys()))

content_recommendations = {}
for user, pref in content_preferences.items():
    content_recommendations[user] = random.choice(content[pref])

for user in users:
    print(f"{user}'s content recommendation: {content_recommendations.get(user)}")