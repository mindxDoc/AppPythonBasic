print("Cùng bạn làm toán")
print("------------------")

# Define the questions and answers as variables
question1 = "Câu 1. 2 luỹ thừa 4 bằng mấy?"
answer1 = 16

question2 = "Câu 2. Căn bậc 3 của 64 là?"
answer2 = 4

question3 = "Câu 3. 78 có chia hết cho 3 không? Bấm Y nếu là Có hoặc N nếu là Không:"
answer3 = "Y"

# Keep track of the score
score = 0

# Ask the user each question and check the answer
user_answer = int(input(question1 + " "))
if user_answer == answer1:
    print("Chính xác!")
    score += 1
else:
    print("Chưa chính xác!")

user_answer = int(input(question2 + " "))
if user_answer == answer2:
    print("Chính xác!")
    score += 1
else:
    print("Chưa chính xác!")

user_answer = input(question3 + " ")
if user_answer == answer3:
    print("Chính xác!")
    score += 1
else:
    print("Chưa chính xác!")

# Print the final score
print("Điểm của bạn là:", score, "trên 3")
