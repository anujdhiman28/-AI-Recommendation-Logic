# AI Recommendation System

A simple **Rule-Based AI Recommendation System** built with Python. This project recommends items based on user interests by calculating a similarity score between user preferences and predefined item tags.

## 📌 Features

- Accepts user interests as input.
- Uses predefined item categories and tags.
- Calculates similarity between user interests and item tags.
- Displays the top 3 matching recommendations.
- Beginner-friendly Python project with clean and readable code.

## 🛠️ Technologies Used

- Python 3
- Basic Python Data Structures (Dictionary, List)
- Functions
- String Manipulation
- Sorting Algorithm

## 📂 Project Structure

```
AI-Recommendation-System/
│── recommendation_system.py
│── README.md
```

## 🚀 How It Works

1. The user enters interests separated by commas.
2. The system compares these interests with tags assigned to each item.
3. A match score is calculated using:

```
Match Score = Number of Matching Tags / Total Tags of the Item
```

4. Items are sorted based on their scores.
5. The top 3 recommendations are displayed.

## 📊 Sample Input

```
Enter your interests:
programming, learning
```

## 📊 Sample Output

```
=== AI Recommendation System ===

Your Recommendations

1. Python Book (Match: 67%)
2. GitHub Course (Match: 67%)
3. AI Guide (Match: 67%)
```

## 🧠 Recommendation Logic

Each item contains predefined tags.

Example:

| Item | Tags |
|------|------|
| Python Book | programming, learning, python |
| GitHub Course | programming, git, learning |
| Yoga Mat | fitness, wellness, health |

The recommendation score is calculated by counting how many user interests match an item's tags.

## 📈 Future Improvements

- GUI using Tkinter
- Machine Learning-based recommendation engine
- User profile storage
- Item ratings and reviews
- Content-Based Filtering
- Collaborative Filtering
- Database integration (SQLite/MySQL)
- Web version using Flask or Django

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/your-username/AI-Recommendation-System.git
```

Go to the project directory:

```bash
cd AI-Recommendation-System
```

Run the program:

```bash
python recommendation_system.py
```

## 🎯 Learning Outcomes

This project helps in understanding:

- Rule-Based Recommendation Systems
- Content-Based Recommendation Concepts
- Dictionaries and Lists in Python
- Functions and Modular Programming
- Similarity Score Calculation
- Sorting Based on Scores

## 👨‍💻 Author

**Anuj**

AI/ML Enthusiast | Python Developer | Machine Learning Learner

---

⭐ If you found this project useful, consider giving it a Star on GitHub!
