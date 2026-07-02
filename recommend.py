def get_user_preferences():
    """Get user interests"""
    print("Enter your interests (comma-separated):")
    interests = input().lower().split(',')
    return [interest.strip() for interest in interests]

def get_available_items():
    """Define available items with tags"""
    items = {
        "Python Book": ["programming", "learning", "python"],
        "GitHub Course": ["programming", "git", "learning"],
        "Yoga Mat": ["fitness", "wellness", "health"],
        "Running Shoes": ["fitness", "sports", "health"],
        "AI Guide": ["programming", "ai", "learning"],
        "Meditation App": ["wellness", "health", "mindfulness"],
        "Coffee Maker": ["kitchen", "appliances", "coffee"],
    }
    return items

def calculate_match_score(user_prefs, item_tags):
    """Calculate similarity score between user preferences and item tags"""
    matches = sum(1 for pref in user_prefs if pref in item_tags)
    return matches / len(item_tags) if item_tags else 0

def recommend_items(user_prefs, items, top_n=3):
    """Generate recommendations based on user preferences"""
    scores = {}
    
    for item_name, tags in items.items():
        score = calculate_match_score(user_prefs, tags)
        scores[item_name] = score
    
   
    recommendations = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return recommendations[:top_n]

def main():
    print("=== AI Recommendation System ===\n")
    
    user_prefs = get_user_preferences()
    items = get_available_items()
    
    recommendations = recommend_items(user_prefs, items)
    
    print("\n Your Recommendations")
    if recommendations[0][1] > 0:
        for idx, (item, score) in enumerate(recommendations, 1):
            print(f"{idx}. {item} (Match: {score*100:.0f}%)")
    else:
        print("No matching recommendations found.")

if __name__ == "__main__":
    main()