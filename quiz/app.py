from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Quiz questions for each difficulty level
quiz_data = {
    "easy": [
        {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4"},
        {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
        {"question": "What is the largest ocean?", "options": ["Atlantic", "Indian", "Arctic", "Pacific"], "answer": "Pacific"},
        {"question": "What is the smallest prime number?", "options": ["1", "2", "3", "5"], "answer": "2"},
        {"question": "What is the capital of Japan?", "options": ["Beijing", "Seoul", "Tokyo", "Bangkok"], "answer": "Tokyo"},
        {"question": "What is 10 - 5?", "options": ["2", "3", "5", "7"], "answer": "5"},
        {"question": "What is the capital of Australia?", "options": ["Sydney", "Melbourne", "Canberra", "Perth"], "answer": "Canberra"},
        {"question": "What is 8 / 2?", "options": ["2", "3", "4", "5"], "answer": "4"},
        {"question": "What is the capital of Canada?", "options": ["Toronto", "Vancouver", "Ottawa", "Montreal"], "answer": "Ottawa"}
    ],
    "medium": [
        {"question": "What is 5 * 5?", "options": ["20", "25", "30", "35"], "answer": "25"},
        {"question": "What is the largest planet?", "options": ["Earth", "Jupiter", "Saturn", "Mars"], "answer": "Jupiter"},
        {"question": "What is the capital of Germany?", "options": ["Berlin", "Munich", "Hamburg", "Frankfurt"], "answer": "Berlin"},
        {"question": "What is 7 * 3?", "options": ["21", "24", "28", "30"], "answer": "21"},
        {"question": "What is the capital of Brazil?", "options": ["Rio de Janeiro", "Brasília", "São Paulo", "Salvador"], "answer": "Brasília"},
        {"question": "What is 15 - 7?", "options": ["6", "7", "8", "9"], "answer": "8"},
        {"question": "What is the capital of Italy?", "options": ["Rome", "Milan", "Venice", "Florence"], "answer": "Rome"},
        {"question": "What is 9 * 2?", "options": ["16", "18", "20", "22"], "answer": "18"},
        {"question": "What is the capital of Spain?", "options": ["Barcelona", "Madrid", "Valencia", "Seville"], "answer": "Madrid"}
    ],
    "hard": [
        {"question": "What is the square root of 64?", "options": ["6", "7", "8", "9"], "answer": "8"},
        {"question": "Who wrote 'To Kill a Mockingbird'?", "options": ["Harper Lee", "Mark Twain", "J.K. Rowling", "Ernest Hemingway"], "answer": "Harper Lee"},
        {"question": "What is 12 * 12?", "options": ["144", "121", "132", "156"], "answer": "144"},
        {"question": "What is the capital of Russia?", "options": ["Moscow", "St. Petersburg", "Kazan", "Sochi"], "answer": "Moscow"},
        {"question": "What is 18 / 3?", "options": ["5", "6", "7", "8"], "answer": "6"},
        {"question": "What is the capital of China?", "options": ["Shanghai", "Beijing", "Guangzhou", "Shenzhen"], "answer": "Beijing"},
        {"question": "What is 20 - 9?", "options": ["10", "11", "12", "13"], "answer": "11"},
        {"question": "What is the capital of India?", "options": ["Mumbai", "Delhi", "Bangalore", "Kolkata"], "answer": "Delhi"},
        {"question": "What is 7 * 7?", "options": ["49", "56", "63", "70"], "answer": "49"},
        {"question": "What is the capital of South Africa?", "options": ["Cape Town", "Pretoria", "Johannesburg", "Durban"], "answer": "Pretoria"}
    ]
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quiz/<difficulty>", methods=["GET", "POST"])
def quiz(difficulty):
    if request.method == "POST":
        score = 0
        for i, question in enumerate(quiz_data[difficulty]):
            user_answer = request.form.get(f"q{i}")
            if user_answer == question["answer"]:
                score += 1
        return redirect(url_for("result", score=score, total=len(quiz_data[difficulty])))
    return render_template(f"{difficulty}.html", questions=quiz_data[difficulty])

@app.route('/quiz-result')
def quiz_result():
    score = 8  # Example score
    total = 10  # Example total
    return render_template('quiz_result.html', score=score, total=total)

if __name__ == "__main__":
    app.run(debug=True)