# List of questions and their correct answers
questions = [
    ["Which language was used to create Facebook?", "Python", "French", "JavaScript", "Php", 4],
    ["What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome", 3],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Saturn", 2],
    ["Who wrote 'Harry Potter'?", "J.K. Rowling", "J.R.R. Tolkien", "Agatha Christie", "Stephen King", 1],
    ["What is the smallest prime number?", "0", "1", "2", "3", 3],
    ["Which element has the chemical symbol 'O'?", "Gold", "Oxygen", "Silver", "Iron", 2],
    ["What is the square root of 64?", "6", "7", "8", "9", 3],
    ["Who painted the Mona Lisa?", "Vincent Van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet", 2],
    ["What is the capital of Japan?", "Seoul", "Tokyo", "Beijing", "Bangkok", 2],
    ["Which is the longest river in the world?", "Nile", "Amazon", "Yangtze", "Mississippi", 2],
    ["Who is known as the 'Father of Computers'?", "Alan Turing", "Bill Gates", "Charles Babbage", "Steve Jobs", 3],
    ["What is the boiling point of water?", "90°C", "95°C", "100°C", "105°C", 3],
    ["What is the hardest natural substance on Earth?", "Gold", "Iron", "Diamond", "Platinum", 3],
    ["Which is the largest ocean on Earth?", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", 4],
    ["What is the capital of Australia?", "Sydney", "Canberra", "Melbourne", "Perth", 2],
    ["What is the chemical symbol for Gold?", "Go", "G", "Au", "Ag", 3],
    ["Who developed the theory of relativity?", "Isaac Newton", "Galileo Galilei", "Nikola Tesla", "Albert Einstein", 4]
]

# Prize levels
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 7500000, 10000000, 75000000]

money = 0

for i in range(len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(question[0])
    print(f"a. {question[1]}        b. {question[2]}")
    print(f"c. {question[3]}        d. {question[4]}")
    
    reply = int(input("Enter your answer (1-4) or 0 to quit:\n"))
    
    if reply == 0:
        money = levels[i-1] if i > 0 else 0
        break
    
    if reply == question[-1]:
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if i == len(questions) - 1:
            money = levels[i]  # The player has answered all questions correctly
        elif i == 4:
            money = 10000
        elif i == 9:
            money = 320000
        elif i == 14:
            money = 7500000
    else:
        print("Wrong answer!")
        if i > 14:
            money = 7500000
        elif i > 9:
            money = 320000
        elif i > 4:
            money = 10000
        else:
            money = 0
        break

print(f"Your take home money is Rs. {money}")
