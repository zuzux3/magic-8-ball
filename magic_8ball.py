import random

name = str (input ("Give me your name: "))

while True: 
    print("Ask Yes-No question:\n")
    print("Type \"End\" if you want to quit program.\n")
    user_question = input()

    if user_question == "End" or user_question == "end" or user_question == "END":
        print ("Goodbye!")
        break

    else:
        random_number = random.randint(1, 9)
        
        if random_number == 1:
            answer = "Yes - definitely."

        elif random_number == 2:
            answer = "It is decidedly so."

        elif random_number == 3:
            answer = "Without a doubt."

        elif random_number == 4:
            answer = "Ask again later."

        elif random_number == 5:
            answer = "Reply hazy, try again."

        elif random_number == 6:
            answer = "Better not tell you now."

        elif random_number == 7:
            answer = "My sources say no."

        elif random_number == 8:
            answer = "Outlook not so good."

        elif random_number == 9:
            answer = "Very doubtful."

        else:
            answer = "Error"

        output_1 = "{} asks: {}"
        output_2 = "Magic 8-Ball's answer: {}"
        print (output_1.format (name, user_question))
        print (output_2.format(answer))
