from PIL import Image
filename = 'guess_who.jpg'
img = Image.open('/Users/arnav007/Library/CloudStorage/Dropbox/Code/Guess Who/guess_who.jpg')
# img = Image.open('C:/Users/Arnav/Desktop/code/Guess Who/guess_who.jpg')
img.show()

print("Welcome to Guess Who 1987! Please choose a character from the image and I will guarantee I will guess your character!")

is_male = input("Is your character a male? (Y/N): ")

if is_male == "Y":
    male_with_hat = input("Does your character have a hat? (Y/N): ")
    if male_with_hat == "Y":
        male_with_green_hat = input("Is the colour of your character's hat green? (Y/N): ")
        if male_with_green_hat == 'Y':
            print("Your character is Bernard!")
        else:
            yellow_hair_male_with_hat = input("Is the hair colour of your character yellow? (Y/N): ")
            if yellow_hair_male_with_hat == "Y":
                print("Your character is Eric!")
            else:
                print("Your character is George!")
    else:
        bald_male = input("Is your character bald? (Y/N): ")
        if bald_male == "Y":
            bald_male_with_glasses = input("Does your character have glasses? (Y/N): ")
            if bald_male_with_glasses == "Y":
                black_hair_bald_male_with_glasses = input("Does your character have black hair? (Y/N): ")
                if black_hair_bald_male_with_glasses == "Y":
                    print("Your character is Tom!")
                else:
                    print("Your character is Sam!")
            else:
                bald_male_facial_hair = input("Does your character have facial hair? (Y/N): ")
                if bald_male_facial_hair == "Y":
                    bald_male_orange_facial_hair = input("Is your character's facial hair orange? (Y/N): ")
                    if bald_male_orange_facial_hair == "Y":
                        print("Your character is Bill!")
                    else:
                        print("Your character is Richard!")
                else:
                    print("Your character is Herman!")
        else:
            orange_hair_male = input("Does your character have orange hair? (Y/N): ")
            if orange_hair_male == "Y":
                orange_facial_hair_male = input("Does your character have facial hair? (Y/N): ")
                if orange_facial_hair_male == "Y":
                    print("Your character is Alfred!")
                else:
                    print("Your character is Frans!")
            else:
                white_hair_male = input("Does your character have white hair? (Y/N): ")
                if white_hair_male == "Y":
                    print("Your character is Peter!")
                else:
                    brown_hair_male = input("Does your character have brown hair? (Y/N): ")
                    if brown_hair_male == "Y":
                        print("Your character is Robert!")
                    else:
                        yellow_hair_male = input("Does your character have yellow hair? (Y/N): ")
                        if yellow_hair_male == "Y":
                            yellow_hair_male_with_glasses = input("Does your character have glasses? (Y/N): ")
                            if yellow_hair_male_with_glasses == "Y":
                                print("Your character is Joe!")
                            else:
                                yellow_hair_male_with_mustache = input("Does your character have a mustache? (Y/N): ")
                                if yellow_hair_male_with_mustache == "Y":
                                    print("Your character is Charles!")
                                else:
                                    print("Your character is David!")
                        else:
                            black_hair_male = input("Does your character have black hair? (Y/N): ")
                            if black_hair_male == "Y":
                                black_hair_male_with_beard = input("Does your character have a beard? (Y/N): ")
                                if black_hair_male_with_beard == "Y":
                                    print("Your character is Philip!")
                                else:
                                    black_hair_male_with_big_nose = input("Does your character have a big nose? (Y/N): ")
                                    if black_hair_male_with_big_nose == "Y":
                                        print("Your character is Max!")
                                    else:
                                        print("Your character is Alex!")



else:
    white_hair_female = input("Is the colour of your character's hair white? (Y/N): ")
    if white_hair_female == "Y":
        white_with_glasses_female = input("Does your character have glasses? (Y/N): ")
        if white_with_glasses_female == "Y":
            print("Your character is Paul!")
        else:
            print("Your character is Susan!")
    else:
        female_with_hat = input("Does your character have a hat? (Y/N): ")
        if female_with_hat == "Y":
            female_with_green_hat = input("Is the colour of your character's hat green? (Y/N): ")
            if female_with_green_hat == "Y":
                print("Your character is Maria!")
            else:
                print("Your character is Claire!")
        else:
            female_with_black_hair = input("Is your character's hair black? (Y/N): ")
            if female_with_black_hair == "Y":
                print("Your character is Anne!")
            else: 
                print("Your character is Anita!")
