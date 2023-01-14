questions = [
    [
        "Besides Sachin Tendulkar, who is the only other Indian cricketer to have scored over 13,000 runs in test cricket?",
        "Virat Kohli", "Sunil Gavaskar", "VVS laxman", "RahulDravid", 4
    ],
    [
        "Ranthambore, Sariska and Keoladeo Ghana are allnames of what?",
        "National Parks", "Goosebumps", "Mountains", "Rivers", 1
    ],
    [
        "India’s official entry to Oscars 2021,Jallikattu” is, a film in which language?",
        "Hindi", "Punjabi", "Kannada", "Malayalam", 4
    ],
    [
        "In terms of production, which of these is the largest train coach manufacturing unit in the  world?",
        "Integral Coach Factory,Bangalore", "Integral Coach Factory,Mumbai",
        "Integral Coach Factory,Chennai", "Integral CoachFactory, Kolkata", 3
    ],
    [
        "In 2020, Louise Gluck won the Nobel Prize in which category?",
        "Music", "Sports", "Literature", "Dance", 3
    ],
    [
        "Which of the following companies was originally started as a loom manufacturing unit in 1909?",
        "Suzuki", "CEAT", "Honda", "Mercedes", 1
    ],
    [
        "In 1994, who became the winner of the first-ever Filmfare R D Burman Award for New Music Talent?",
        "Udit Narayan", "A.R.Rahman", "Lata Mangeshkar", "Raj Burman", 2
    ],
    [
        "What colour did Lord Shiva’s throat turn into when he drank the deadly poison during Samudra Manthan?",
        "Red", "Yellow", "Blue", "Black", 3
    ],
    [
        "What is the profession of Kabir in the film Kabir Singh?", "Engineer",
        "Cricketor", "Athlete", "Doctor", 4
    ],
    [
        "Which of these national parks is named after the river that flows through the park?",
        "Pench", "Tadoba", "Vrindavan", "Wildera", 1
    ]
]

levels = [
    "1000", "2000", "5000", "10000", "20000", "50000", "100000", "500000",
    "1000000", "3000000"
]
money = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n Question for Rs.{levels[i]} in front of your screen ")
    print("\n", question[0])

    print(f"\n a.{question[1]} \t\t b.{question[2]}")
    print(f"\n c.{question[3]} \t\t d.{question[4]}")

    reply = int(input("\n Enter your answer {1-4} or 0 to quit"))

    if (reply == 0):
        break

    if (reply == question[-1]):
        print(f"\n****Correct answer you won Rs.{levels[i]}****")

        # User will take home some money after below questions
        # he will not loose everything

        if (i == 3):
            money = 10000
        elif (i == 6):
            money = 100000
        elif (i == 9):
            money = 3000000
            print("A Very Congratulations you have cleared a final level")

    else:
        print("Wrong answer!")
        break

print(f"\n Your take home money is {money} ")
