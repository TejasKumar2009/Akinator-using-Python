from multiprocessing.connection import answer_challenge
from statistics import correlation
import akinator

aki = akinator.Akinator()
q = aki.start_game()

while aki.progression <= 80:
    ask_ques = input(f"{q} : ")
    if ask_ques == 'b':
        try:
            q = aki.back()
        except akinator.CantGoBackAnyFurther:
            print("Akinator Cannot Go Back Any Further!")
    else:
        answer = akinator.Answer.from_str(ask_ques)
        q = aki.answer(answer)
        try:
            answer = akinator.Answer.from_str(ask_ques)
        except akinator.InvalidAnswer:
            print("Invalid Answer!")

aki.win()
print(f"\nName : {aki.first_guess.name}")
print(f"Description : {aki.first_guess.description}")
print(f"Image : {aki.first_guess.absolute_picture_path}")

correct = input("Is it correct : ")

f1 = open("total.txt", "r")
f1total_str = f1.read()
f1total = int(f1total_str)
f1total+=1

f2 = open("total.txt", "w")
f2.write(str(f1total))
f2.close()

if correct.lower() == "yes" or correct.lower() == "y":
    print("Yeah!! I got it :)")
    f3 = open("win.txt", "r")
    f3total_str = f3.read()
    f3total = int(f3total_str)
    f3total+=1

    f4 = open("win.txt", "w")
    f4.write(str(f3total))
    f4.close()


else:
    f5 = open("loose.txt", "r")
    f5total_str = f5.read()
    f5total = int(f5total_str)
    f5total+=1

    f6 = open("loose.txt", "w")
    f6.write(str(f5total))
    f6.close()


f_win = open("win.txt", "r")
f_win_total_str = f_win.read()
f_win_total = int(f_win_total_str)

f_loose = open("loose.txt", "r")
f_loose_total_str = f_loose.read()
f_loose_total = int(f_loose_total_str)


print(f"\n By The Way You Know I have Won {f_win_total}/{f1total} Challenges! My Win Percent is {round(f_win_total*100/f1total, 1)}% :))")
