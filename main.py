from tkinter import *
import random
import copy

COURSE_FILE = "ma323.txt"

# creating the tkinter window
main = Tk()
main.title("FlashCard")
main.geometry("1500x200")
main.configure(bg="gray")

# variables
main_text = "Click Next to Start"
quiz_text = ""
card_text = ""
quiz_count = 0
quiz = False
file_list = []
index = 0

# file read
f = open(COURSE_FILE, "r", encoding='utf-8')

for line in f.readlines():
    file_list.append(line)
f.close()

for i in range(len(file_list)):
    file_list[i] = file_list[i].strip("\n").split('&')

main_list = copy.deepcopy(file_list)

# functions
def flip():
    global main_text
    global card_text
    global index
    
    if (card_text == "Front"):
        card_text = "Back"
    elif (card_text == "Back"):
        card_text = "Front"
    card_label.config(text = card_text)
    
    if (main_text == main_list[index][0]):
        main_text = main_list[index][1]
        if (len(main_text) > 150):
            main_text = main_text[:149] + "\n" + main_text[149:]
    elif (main_text == main_list[index][1] or main_text == main_list[index][1][:149] + "\n" + main_list[index][1][149:]):
        main_text = main_list[index][0]
    main_label.config(text = main_text)
def advance():
    global quiz
    global quiz_count
    global main_list
    global main_text
    global card_text
    global index
    
    if (quiz):
        if (quiz_count >= len(file_list)):
            quiz_count = 1
            quiz_label.config(text = "Quiz complete, restarting -> " + quiz_text + str(quiz_count) + "/" + str(len(file_list)))
            main_list = copy.deepcopy(file_list)
        else:
            del main_list[index]
            quiz_count += 1
            quiz_label.config(text = quiz_text + str(quiz_count) + "/" + str(len(file_list)))
    
    card_text = "Front"
    card_label.config(text = card_text)
    
    index = random.randint(0, len(main_list) - 1)
    main_text = main_list[index][0]
    main_label.config(text = main_text)
def set_quiz():
    global quiz
    global quiz_text
    global quiz_count
    global file_list
    global main_list
    global main_text
    global card_text
    global index
    
    quiz = True
    quiz_text = "Quiz: "
    quiz_count = 1
    quiz_label.config(text = quiz_text + str(quiz_count) + "/" + str(len(file_list)))
    
    card_text = "Front"
    card_label.config(text = card_text)
    
    main_list = copy.deepcopy(file_list)
    index = random.randint(0, len(main_list) - 1)
    main_text = main_list[index][0]
    main_label.config(text = main_text)
def set_random():
    global quiz
    global quiz_text
    global file_list
    global main_list
    global main_text
    global card_text
    global index
    
    quiz = False
    quiz_text = ""
    quiz_label.config(text = quiz_text)
    
    card_text = "Front"
    card_label.config(text = card_text)
    
    main_list = copy.deepcopy(file_list)
    index = random.randint(0, len(main_list) - 1)
    main_text = main_list[index][0]
    main_label.config(text = main_text)

# button widgets
flip_button = Button(main, text = "Flip", command = flip)
next_button = Button(main, text = "Next", command = advance)
quiz_button = Button(main, text = "Quiz", command = set_quiz, bg="red")
random_button = Button(main, text = "Random", command = set_random, bg="blue")

# label widgets
main_label = Label(main, text = main_text, font=("Arial", 15), bg="gray")
quiz_label = Label(main, text = quiz_text, fg="white", bg="gray")
card_label = Label(main, text = card_text, fg="black", bg="gray")

# pack the widgets
quiz_label.pack(side=TOP)
main_label.pack(side=TOP)
card_label.pack(side=TOP)
random_button.pack(side=BOTTOM)
quiz_button.pack(side=BOTTOM)
next_button.pack(side=BOTTOM)
flip_button.pack(side=BOTTOM)

# start GUI
main.mainloop()