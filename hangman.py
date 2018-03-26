import random
def hangman():
   
    while True:
        print("1. capitals\n2. animals\n3. countries\n4. ideas\n")
        category = (input("Please choose a category by pressing its number:"))
        if category == '1':
            list1 = open("/home/havszab/codes/python/categories/capitals.txt", "r")
            capitals = [line.rstrip("\n") for line in list1]
            choice = random.choice(capitals)
            list1.close()
            break 
        elif category == "2":
            list2 = open("/home/havszab/codes/python/categories/animals.txt", "r")
            animals = [line.rstrip('\n') for line in list2]
            choice = random.choice(animals)
            list2.close()
            break
        elif category == "3":
            list3 = open("/home/havszab/codes/python/categories/countries.txt", 'r')
            countries = [line.rstrip('\n') for line in list3]
            choice = random.choice(countries)
            list3.close()
            break
        elif category == "4":
            list4 = open("/home/havszab/codes/python/categories/ideas.txt", 'r')
            ideas = [line.rstrip('\n') for line in list4]
            choice = random.choice(ideas)
            list4.close()
            break  
        else:
            print('Please select an existing category. ')
    
    print('_ ' * len(choice))
    choice = [item.lower() for item in choice]
  

    underscore_list = list("_" * len(choice))
    indices = []
    wrong_tips = []
    lives_left = 10

    while len(indices) != len(choice):
        index = int(0)
        guess = input(str('Enter a letter please!'))
        list(choice)  
        if guess in choice:   
            while index != len(choice):
                if choice[index] == guess:
                    underscore_list.insert(index, guess)
                    del underscore_list[index + 1]
                    indices.append(index)
                    print("\n")
                index = index + 1
        else:
            if len(guess) > 1: #ha több betű
                print('One letter is enough, please retype.')
            elif guess in ['1','2','3','4','5','6','7','8','9','0']:#ha valamelyik szám
                print('Words contain only letters, so enter one of them please.') 
            elif guess in wrong_tips:#ha már volt
                print('Don\'t make the same mistake twice!')
            else:#ha csak simán rossz
                wrong_tips.append(guess)
                lives_left -= 1    
        if lives_left == 0:
            print('The word was: ', *choice)
            print('You have been executed.') 
            break
        print(*underscore_list, "\n")
        print("Wrong tips: ", wrong_tips)
        print('Remaining mistakes: ', lives_left)
    if choice[index-1] == guess:
        print('You won, so you survived')
            
    while True: 
        rematch_input = input(str('Do you want to play again? (y/n)'))
        if rematch_input == 'y':
            hangman()
        elif rematch_input == 'n':
            exit()
        else:
            print('Please choose between y or n. ')
            

hangman()







    








