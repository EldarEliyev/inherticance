# # #Number Game project:
# # # import random
# # # print("Hi welcome to the game,This is a number guessing game. \nYou got 7 chances to guess the number.Let's start the game")
# # # number_to_guess = random.randrange(100)
# # # chances = 7
# # # guess_counter = 0

# # # while guess_counter <chances:
# # #     guess_counter +=1
# # #     my_guess = int(input("Please Enter your Guess:"))
    
# # #     if my_guess == number_to_guess:
# # #         print(f'The number is {number_to_guess} and you found it right !! in the {guess_counter} attempt')
# # #         break
# # #     elif guess_counter >= chances and my_guess != number_to_guess:
# # #         print(f'Oops sorry, The number is {number_to_guess} better luck next time')
        
# # #     elif my_guess > number_to_guess:
# # #         print('Your guess is higher')
        
# # #     elif my_guess <number_to_guess:
# # #         print('Your guess is lesser')


# # # For word Guessing Game
# # # import random
# # # name = input("What is your name?")
# # # print("Good Luck! ", name)
# # # words = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board', 'geeks']
# # # word = random.choice(words)
# # # print("Guess the characters")

# # # guesses = ''
# # # turns = 12

# # # while turns >0:
# # #     failed = 0
# # #     for char in word:
# # #         if char in guesses:
# # #             print(char, end=" ")
            
# # #         else:
# # #             print("__")
# # #             failed +=1
            
# # #             if failed ==0:
# # #                 print("You win")
# # #                 print("The word is:", word)
# # #                 break
# # #             print()
# # #             guess = input("Guess a character:")
# # #             guesses +=guess
            
# # #             if guess not in word:
# # #                 turns -=1
# # #                 print("Wrong")
# # #                 print("You have", +turns, 'more guesses')
                
# # #                 if turns ==0:
# # #                     print("You Loose")




# # #Hangman Game
# # # import random
# # # from collections import Counter
# # # some_words = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon'''
# # # some_words = some_words.split(' ')
# # # word = random.choice(some_words)
# # # if __name__ == '__main__':
# # #     print('Guess the word! HINT: word is a name of a fruit')
    
# # #     for i in word:
# # #         print('_',end=' ')
# # #         print()
        
# # #         playing = True
# # #         letter_Guessed = ''
# # #         chances = len(word)+2
# # #         correct = 0
# # #         flag = 0
        
# # #         while (chances !=0) and flag ==0:
# # #                 print()
# # #                 chances -=1
# # #                 try:
# # #                     guess = str(input('Enter a letter to guess:'))
# # #                 except:
# # #                     print('Enter only a letter!')
# # #                     continue
# # #                 if not guess.isalpha():
# # #                     print('Enter only a LETTER')
# # #                     continue
# # #                 elif len(guess) >1:
# # #                     print("Enter only a SINGLE letter")
# # #                     continue
# # #                 elif guess in letter_Guessed:
# # #                     print('You have already guessed that letter')
# # #                     continue
                
# # #                 if guess in word:
# # #                     k = word.count(guess)
                    
# # #                     for _ in range(k):
# # #                         letter_Guessed +=guess
                        
# # #                         for char in word:
# # #                             if char in letter_Guessed and (Counter(letter_Guessed)) != Counter(word):
# # #                                 print(char, end=' ')
# # #                                 correct +=1
# # #                             elif(Counter(letter_Guessed)) == Counter(word):
# # #                                 print("The word is:", end=' ')
# # #                                 print(word)
# # #                                 flag = 1
# # #                                 print('Congratulations , You won!')
# # #                                 break
# # #                             break
# # #                         else:
# # #                             print('_',end=' ')
                            
# # #                             if chances <=0 and (Counter(letter_Guessed)) != Counter(word):
# # #                                 print()
# # #                                 print('You lost! Try again.')
# # #                                 print('The word was {}'.format(word))
            

# # # #21 Number Game
# # # def nearestMultiple(num):
# # #     if num >=4:
# # #         near = num+ (4-(num %4))
# # #     else:
# # #         near = 4
# # #         return near
    

# # # def lose1():
# # #     print("\n\nYOU LOSE!")
# # #     print("Better luck next time!")
# # #     exit(0)
    
# # # def check(xyz):
# # #     i = 1
# # #     while i<len(xyz):
# # #         if (xyz[i]- xyz[i-1]) !=1:
# # #             return False
# # #         i = i+1
# # #         return True
    
# # # def start1():
# # #     xyz = []
# # #     last = 0
# # #     while True:
# # #         print("Enter 'F' to take the first chance.")
# # #         print("Enter 'S' to take the second chance.")
# # #         chance = input('>')
        
# # #         if chance == "F":
# # #             while True:
# # #                 if last ==20:
# # #                     lose1()
# # #                 else:
# # #                     print("\nYour Turn.")
# # #                     print("\nHow many numbers do you wish to enter?")
# # #                     inp = int(input('>'))
                    
# # #                     if inp>0 and inp <=3:
# # #                         comp = 4-inp
# # #                     else:
# # #                         print("Wrong input.You are disqualified  from the game.")
# # #                         lose1()
                        
# # #                         i,j = 1,1
# # #                         print("Now enter the values")
# # #                         while i<=inp:
# # #                             a = input('>')
# # #                             a = int(a)
# # #                             xyz.append(a)
# # #                             i = i+1
                            
# # #                             last = xyz[-1]
                            
# # #                             if check (xyz) == True:
# # #                                 if last == 21:
# # #                                     lose1()
                                    
# # #                                 else:
# # #                                     while j <= comp:
# # #                                      xyz.append(last+j)
# # #                                      j= j+1
# # #                                      print("Order of inputs after computer's turn is:")
# # #                                      print(xyz)
# # #                                      last = xyz[-1] 
# # #                                     else:
# # #                                         print("\nYou did not input consecutive integers.")
# # #                                         lose1()
                                        
# # #                                          elif chance == "S":
# # #             comp = 1
# # #             last = 0
# # #             while last < 20:
# # #                 #"Computer's turn"
# # #                 j = 1
# # #                 while j <= comp:
# # #                     xyz.append(last + j)
# # #                     j = j + 1
# # #                 print ("Order of inputs after computer's turn is:")
# # #                 print (xyz)
# # #                 if xyz[-1] == 20:
# # #                     lose1()
                     
# # #                 else:
# # #                     print ("\nYour turn.")
# # #                     print ("\nHow many numbers do you wish to enter?")
# # #                     inp = input('> ')
# # #                     inp = int(inp)
# # #                     i = 1
# # #                     print ("Enter your values")
# # #                     while i <= inp:
# # #                         xyz.append(int(input('> ')))
# # #                         i = i + 1
# # #                     last = xyz[-1]
# # #                     if check(xyz) == True:
# # #                         # print (xyz)
# # #                         near = nearestMultiple(last)
# # #                         comp = near - last
# # #                         if comp == 4:
# # #                             comp = 3
# # #                         else:
# # #                             comp = comp
# # #                     else:
# # #                         # if inputs are not consecutive
# # #                         # automatically disqualified
# # #                         print ("\nYou did not input consecutive integers.")
# # #                         # print ("You are disqualified from the game.")
# # #                         lose1()
# # #             print ("\n\nCONGRATULATIONS !!!")
# # #             print ("YOU WON !")
# # #             exit(0)
             
# # #         else:
# # #             print ("wrong choice")
                         
         
# # # game = True   
# # # while game == True:
# # #         print ("Player 2 is Computer.")
# # #         print("Do you want to play the 21 number game? (Yes / No)")
# # #         ans = input('> ')
# # #         if ans =='Yes':
# # #             start1()
# # #         else:
# # #             print ("Do you want quit the game?(yes / no)")
# # #             nex = input('> ')
# # #             if nex == "yes":
# # #                 print ("You are quitting the game...")
# # #                 exit(0)
# # #             elif nex == "no":
# # #                 print ("Continuing...")
# # #             else:
# # #                 print ("Wrong choice")
                                        
                                        
                                             
  
# # #Mastermind Game
# # # import random
# # # num = random.randrange(1000,10000)
# # # n = int(input('Guess the 4 digit number:'))
# # # if(n == num):
# # #     print("Great! You guessed the number in just 1 try! You're a Mastermind!")
# # # else:
# # #     ctr = 0
    
# # #     while(n!= num):
# # #         ctr +=1
# # #         count = 0
# # #         n = str(n)
# # #         num = str(num)
# # #         correct = []
        
# # #         for i in range(0,4):
# # #             if(n[i] == num[i]):
# # #                 count +=1
# # #                 correct.append(n[i])
# # #             else:
# # #                 continue
# # #             if(count <4) and (count != 0):
# # #                 print("Not quite the number. But you did get ",
# # #                   count, " digit(s) correct!")
# # #                 print("Also these numbers in your input were correct.")
                
# # #                 for k in correct:
# # #                     print(k,end=' ')
                    
# # #                     print("\n")
# # #                     print("\n")
# # #                     n = int(input("Enter your next choice of numbers:"))
# # #             elif (count == 0):
# # #                 print("None of the numbers in your input match.")
# # #                 n = int(input("Enter your next choice of numbers."))
# # #                 if n == num:
# # #                     print("You've become a Mastermind!")
# # #                     print("It took you only", ctr, "tries")

# # #Flames Game
# # # def remove_match_char(list1, list2):
 
# # #     for i in range(len(list1)):
# # #         for j in range(len(list2)):
 
# # #             # if common character is found
# # #             # then remove that character
# # #             # and return list of concatenated
# # #             # list with True Flag
# # #             if list1[i] == list2[j]:
# # #                 c = list1[i]
 
# # #                 # remove character from the list
# # #                 list1.remove(c)
# # #                 list2.remove(c)
 
# # #                 # concatenation of two list elements with *
# # #                 # * is act as border mark here
# # #                 list3 = list1 + ["*"] + list2
 
# # #                 # return the concatenated list with True flag
# # #                 return [list3, True]
 
# # #     # no common characters is found
# # #     # return the concatenated list with False flag
# # #     list3 = list1 + ["*"] + list2
# # #     return [list3, False]
 
 
# # # # Driver code
# # # if __name__ == "__main__":
 
# # #     # take first name
# # #     p1 = input("Player 1 name : ")
 
# # #     # converted all letters into lower case
# # #     p1 = p1.lower()
 
# # #     # replace any space with empty string
# # #     p1.replace(" ", "")
 
# # #     # make a list of letters or characters
# # #     p1_list = list(p1)
 
# # #     # take 2nd name
# # #     p2 = input("Player 2 name : ")
# # #     p2 = p2.lower()
# # #     p2.replace(" ", "")
# # #     p2_list = list(p2)
 
# # #     # taking a flag as True initially
# # #     proceed = True
 
# # #     # keep calling remove_match_char function
# # #     # until common characters is found or
# # #     # keep looping until proceed flag is True
# # #     while proceed:
 
# # #         # function calling and store return value
# # #         ret_list = remove_match_char(p1_list, p2_list)
 
# # #         # take out concatenated list from return list
# # #         con_list = ret_list[0]
 
# # #         # take out flag value from return list
# # #         proceed = ret_list[1]
 
# # #         # find the index of "*" / border mark
# # #         star_index = con_list.index("*")
 
# # #         # list slicing perform
 
# # #         # all characters before * store in p1_list
# # #         p1_list = con_list[: star_index]
 
# # #         # all characters after * store in p2_list
# # #         p2_list = con_list[star_index + 1:]
 
# # #     # count total remaining characters
# # #     count = len(p1_list) + len(p2_list)
 
# # #     # list of FLAMES acronym
# # #     result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
 
# # #     # keep looping until only one item
# # #     # is not remaining in the result list
# # #     while len(result) > 1:
 
# # #         # store that index value from
# # #         # where we have to perform slicing.
# # #         split_index = (count % len(result) - 1)
 
# # #         # this steps is done for performing
# # #         # anticlock-wise circular fashion counting.
# # #         if split_index >= 0:
 
# # #             # list slicing
# # #             right = result[split_index + 1:]
# # #             left = result[: split_index]
 
# # #             # list concatenation
# # #             result = right + left
 
# # #         else:
# # #             result = result[: len(result) - 1]
 
# # #     # print final result
# # #     print("Relationship status :", result[0])



# # # Pokemon Training Game
# # # powers = [3,8,9,7]
# # # mini,maxi = 0,0
# # # for power in powers:
# # #     if mini == 0 and maxi == 0:
# # #         mini,maxi = powers[0], powers[0]
# # #         print(mini,maxi)
# # #     else:
# # #         mini = min(mini,power)
# # #         maxi = max(maxi,power)
# # #         print(mini,maxi)
        


# # #Rock Paper Scissor game
# # # import random
# # # print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
# # #       + "Rock vs Paper -> Paper wins \n"
# # #       + "Rock vs Scissors -> Rock wins \n"
# # #       + "Paper vs Scissors -> Scissors wins \n")
# # # while True:
# # #     print("Enter your chice \n 1-Rock \n 2-Paper \n3 - Scissors \n")
# # #     choice = int(input("Enter your choice:"))
    
# # #     while choice >3 or choice <1:
# # #              choice = int(input('Enter a valid choice please ☺: '))
# # #              if choice == 1:
# # #                  choice_name = 'Rock'
# # #              elif choice == 2:
# # #                  choice_name = 'Paper'
# # #              else:
# # #                  choice_name = 'Scissors'
                 
# # #                  print("User choice is:", choice_name)
# # #                  print("Now it's Computer's Turn...")
# # #                  comp_choice = random.randint(1,3)
                 
# # #                  if comp_choice == 1:
# # #                      comp_choice_name = 'Rock'
# # #                  elif comp_choice == 2:
# # #                      comp_choice_name = 'Paper'
# # #                  else:
# # #                      comp_choice_name = 'Scissors'
                     
# # #                      print("Computer choice is:", comp_choice_name)
# # #                      print(choice_name, 'vs', comp_choice_name)
                     
# # #                      if choice == comp_choice:
# # #                          result = "DRAW"
# # #                      elif(choice == 1 and comp_choice ==2) or (comp_choice == 1 and choice ==2):
# # #                          result = 'Paper'
# # #                      elif(choice == 1 and comp_choice == 3) or (comp_choice == 1 and choice ==3):
# # #                          result = 'Rock'
# # #                      elif (choice == 2 and comp_choice == 3 ) or (comp_choice ==2 and choice ==3):
# # #                          result = 'Scissors'
                         
# # #                          if result == "DRAW":
# # #                              print("<== It's a tie! ==>")
# # #                          elif result == choice_name:
# # #                              print("<== User wins! ==>")
# # #                          else:
# # #                              print("<== Computer wins! ==>")
                             
# # #                              print("Do you want to play again? (Y/N)")
# # #                              ans = input().lower()
# # #                              if ans == 'n':
# # #                                  break
# # #                              print("Thanks for playing!")

# # # Taking Screenshots
# # # import pyscreenshot
# # # image = pyscreenshot.grab()
# # # image._show()
# # # image.SAVE("GeeksforGeeks.png")




# # # Keylogger 
# # import pynput
# # from pynput.keyboard import Key, Listener
  
# # keys = []
  
# # def on_press(key):
     
# #     keys.append(key)
# #     write_file(keys)
     
# #     try:
# #         print('alphanumeric key {0} pressed'.format(key.char))
         
# #     except AttributeError:
# #         print('special key {0} pressed'.format(key))
          
# # def write_file(keys):
     
# #     with open('log.txt', 'w') as f:
# #         for key in keys:
             
# #             # removing ''
# #             k = str(key).replace("'", "")
# #             f.write(k)
                     
# #             # explicitly adding a space after 
# #             # every keystroke for readability
# #             f.write(' ') 
              
# # def on_release(key):
                     
# #     print('{0} released'.format(key))
# #     if key == Key.esc:
# #         # Stop listener
# #         return False
  
  
# # with Listener(on_press = on_press,
# #               on_release = on_release) as listener:
                     
# #     listener.join()



# # Cows and Bulls game
# # import random
# # def getDigits(num):
# #     return [int(i) for i in str(num)]

# # def noDuplicates(num):
# #     num_li = getDigits(num)
# #     if len(num_li) == len(set(num_li)):
# #         return True
# #     else:
# #         return False

# # def generateNum():
# #     while True:
# #         num = random.randint(1000,9999)
# #         if noDuplicates(num):
# #             return num

# # def numOfBullsCows(num,guess):
# #     bull_cow = [0,0]
# #     num_li = getDigits(num)
# #     guess_li = getDigits(guess)
    
# #     for i,j in zip(num_li, guess_li):
# #         if j in num_li:
# #             if j ==i:
# #                 bull_cow[0] +=1
# #             else:
# #                 bull_cow[1] +=1
# #                 return bull_cow
            
# # num = generateNum()
# # tries = int(input('Enter number of tries:'))
# # while tries >0:
# #     guess = int(input("Enter your guess:"))
    
# #     if not noDuplicates(guess):
# #         print("Number should not have repeated digits.Try again.")
# #         continue
# #     if guess <1000 or guess > 9999:
# #         print("Enter 4 digit number only. Try again.")
# #         continue
    
# # bull_cow = numOfBullsCows(num,guess)
# # print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")
# # tries -=1
# # if bull_cow[0] ==4:
# #     print("You guessed right!")
# # else:
# #        print(f"You ran out of tries. Number was {num}") 



# # import json
# # import requests
# # from pywebio.input import*
# # from pywebio.output import*
# # from pywebio.session import*

# # def get_fun_fact(__):
# #     clear()
# #     put_html(
# #         '<p align="left">'
# #         '<h2><img src="https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png" width="7%"> Fun Fact Generator</h2>'
# #         '</p>'
# #     )
# #     url = "https://uselessfacts.jsph.pl/random.json?language=en"
# #     response = requests.get(url)
# #     data = json.loads(response.text)
# #     useless_fact = data['text']
# #     style(put_text(useless_fact), 'color:blue; font-size: 30px')
# #     put_buttons(
# #         [dict(label = 'Click me', value = 'outline-success', color = 'outline-success')],
# #         onclick=get_fun_fact
# #     )
# #     if __name__ == '__main__':
# #         put_html(
# #         '<p align="left">'
# #         '<h2><img src="https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png" width="7%"> Fun Fact Generator</h2>'
# #         '</p>'
# #     )
        
# #         put_buttons(
# #         [dict(label='Click me', value='outline-success', color='outline-success')],
# #         onclick=get_fun_fact
# #     )
# #     hold()
        
        
        
        
# # Check if two PDF documents are identical with Python
# # import hashlib 
# # from difflib import SequenceMatcher 
  
  
# # def hash_file(fileName1, fileName2): 
  
# #     # Use hashlib to store the hash of a file 
# #     h1 = hashlib.sha1() 
# #     h2 = hashlib.sha1() 
  
# #     with open(fileName1, "rb") as file: 
  
# #         # Use file.read() to read the size of file 
# #         # and read the file in small chunks 
# #         # because we cannot read the large files. 
# #         chunk = 0
# #         while chunk != b'': 
# #             chunk = file.read(1024) 
# #             h1.update(chunk) 
              
# #     with open(fileName2, "rb") as file: 
  
# #         # Use file.read() to read the size of file a 
# #         # and read the file in small chunks 
# #         # because we cannot read the large files. 
# #         chunk = 0
# #         while chunk != b'': 
# #             chunk = file.read(1024) 
# #             h2.update(chunk) 
  
# #         # hexdigest() is of 160 bits 
# #         return h1.hexdigest(), h2.hexdigest() 
  
  
# # msg1, msg2 = hash_file("pd1.pdf ", "pd1.pdf") 
  
# # if(msg1 != msg2): 
# #     print("These files are not identical") 
# # else: 
# #     print("These files are identical") 



# # Creating payment receipts using Python
# # from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle 
# # from reportlab.lib import colors 
# # from reportlab.lib.pagesizes import A4 
# # from reportlab.lib.styles import getSampleStyleSheet 
  
# # # data which we are going to display as tables 
# # DATA = [ 
# #     [ "Date" , "Name", "Subscription", "Price (Rs.)" ], 
# #     [ 
# #         "16/11/2020", 
# #         "Full Stack Development with React & Node JS - Live", 
# #         "Lifetime", 
# #         "10,999.00/-", 
# #     ], 
# #     [ "16/11/2020", "Geeks Classes: Live Session", "6 months", "9,999.00/-"], 
# #     [ "Sub Total", "", "", "20,9998.00/-"], 
# #     [ "Discount", "", "", "-3,000.00/-"], 
# #     [ "Total", "", "", "17,998.00/-"], 
# # ] 
  
# # # creating a Base Document Template of page size A4 
# # pdf = SimpleDocTemplate( "receipt.pdf" , pagesize = A4 ) 
  
# # # standard stylesheet defined within reportlab itself 
# # styles = getSampleStyleSheet() 
  
# # # fetching the style of Top level heading (Heading1) 
# # title_style = styles[ "Heading1" ] 
  
# # # 0: left, 1: center, 2: right 
# # title_style.alignment = 1
  
# # # creating the paragraph with  
# # # the heading text and passing the styles of it 
# # title = Paragraph( "GeeksforGeeks" , title_style ) 
  
# # # creates a Table Style object and in it, 
# # # defines the styles row wise 
# # # the tuples which look like coordinates  
# # # are nothing but rows and columns 
# # style = TableStyle( 
# #     [ 
# #         ( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ), 
# #         ( "GRID" , ( 0, 0 ), ( 4 , 4 ), 1 , colors.black ), 
# #         ( "BACKGROUND" , ( 0, 0 ), ( 3, 0 ), colors.gray ), 
# #         ( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.whitesmoke ), 
# #         ( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ), 
# #         ( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.beige ), 
# #     ] 
# # ) 
  
# # # creates a table object and passes the style to it 
# # table = Table( DATA , style = style ) 
  
# # # final step which builds the 
# # # actual pdf putting together all the elements 
# # pdf.build([ title , table ]) 

# # Speak the meaning of the word using Python

# # import pyttsx3
# # from PyDictionary import PyDictionary
 
 
# # class Speaking:
 
# #     def speak(self, audio):
       
# #         # Having the initial constructor of pyttsx3 
# #         # and having the sapi5 in it as a parameter
# #         engine = pyttsx3.init('sapi5')
         
# #         # Calling the getter and setter of pyttsx3
# #         voices = engine.getProperty('voices')
         
# #         # Method for the speaking of the assistant
# #         engine.setProperty('voice', voices[0].id)
# #         engine.say(audio)
# #         engine.runAndWait()
 
 
# # class GFG:
# #     def Dictionary(self):
# #         speak = Speaking()
# #         dic = PyDictionary()
# #         speak.speak("Which word do u want to find the meaning sir")
         
# #         # Taking the string input
# #         query = str(input())
# #         word = dic.meaning(query)
# #         print(len(word))
         
# #         for state in word:
# #             print(word[state])
# #             speak.speak("the meaning  is" + str(word[state]))
 
 
# # if __name__ == '__main__':
# #     GFG()
# #     GFG.Dictionary(self=None)


# # simple arithmetic calculator
# # operator = input("Enter an operator (+ - * /):")
# # num1 = float(input("Enter the 1st number:"))
# # num2 = float(input("Enter the 2nd number:"))

# # if operator == "+":
# #     result = num1+num2
# #     print(round(result,3))
# # elif operator == "-":
# #     result = num1-num2
# #     print(round(result,3))
# # elif operator == "*":
# #     result = num1*num2
# #     print(round(result,3))
# # elif operator == "/":
# #     result = num1/num2
# #     print(round(result,3))
# # else:
# #     print(f"{operator} is not valid operator") 



# #Python weight converter:
# # weight = float(input("Enter your weight:"))
# # unit = input("Kilograms or Pounds? (K or L):")

# # if unit == "K":
# #     weight = weight *2.205
# #     unit = "Lbs."
# #     print(f"Your weight is : {round(weight,1)} {unit}")
# # elif unit == "L":
# #     weight = weight / 2.205
# #     unit = "Kgs."
# #     print(f"Your weight is : {round(weight,1)} {unit}")
# # else:
# #     print(f"{unit} was not valid!")


# #3.temperature conversion
# # unit = input("Is this temperature in Celsius or Fahreneit (C/F):")
# # temp = float(input("Enter the temperature:"))

# # if unit == "C":
# #     temp = round((9*temp)/ 5+32,1)
# #     print(f"The temperature in Fahreneit is : {temp}F.")
# # elif unit == "F":
# #     temp = round((temp -32)*5 / 9,1)
# #     print(f"The temperature in Fahreneit is : {temp}C.")

    
     
# # else:
# #     print(f"{unit} is an invalid unit of measurement")




# #4.email slicer program
# # email = input("Enter your email:")
# # index = email.index("@")
# # username = email[:email.index("@")]
# # domain = email[email.index("@")+ 1:]
# # print(f"Your username is {username} and domain is {domain}")



# #5.Python compound interest calculator
# # principle = 0
# # rate = 0
# # time = 0

# # while True:
# #     principle = float(input("Enter the principle amount:"))
# #     if principle < 0:
# #         print("Principle can't be less than zero")
# #     else:
# #         break
# #     while True:
# #         rate = float(input("Enter the interest rate:"))
# #         if rate <0:
# #             print("Interest rate can't be less than zero")
# #         else:
# #             break
# #         while True:
# #             time = int(input("Enter the time in years:"))
# #             if time <0:
# #                 print("Time can't be less than zero.")
# #             else:
# #                 break   
# # total = principle * pow((1+rate / 100),time)
# # print(f"Balance after {time} year/s : ${total:.2f}")
            
            
        


# #6.Countdown timer
# # import time
# # my_time = int(input("Enter the time in seconds:"))
# # for x in  range(my_time,0, -1):
# #     seconds = x % 60
# #     minutes = int(x / 60) % 60
# #     hours = int(x / 3600)
# #     print(f"{hours:02}:{minutes:02}:{seconds:02}")
# #     time.sleep(1)
# # print("Time's UP!")




# #7.shopping cart program
# # foods = []
# # prices = []
# # total = 0

# # while True:
# #     food = input("Enter a food to buy (q to quit):")
# #     if food.lower() == "q":
# #         break
# #     else:
# #         price = float(input("Enter the price of  a{food}: $"))
# #         foods.append(food)
# #         prices.append(price)
        
# # print("--------Your Cart-------")
# # for food in foods:
# #     print(food,end=" ")
    
    
# #     for price in prices:
# #         total += price
# # print()        
# # print(f"Your total is: ${total}")
    


# #8.Quiz game [INTERMEDIATE]
# # questions = ("How many elements are in the perodic table?:", 
# #              "Which animal lays the largest eggs?:", 
# #              "What is the most abundant gas in Earth's atmosphere?:", 
# #              "How many bones are in the human body?:", 
# #              "Which planet in the solar system is the hottest?:")
# # options = (("A.116", " B.117", "C.118", " D.119"), 
# #            ("A.Whale", " B.Crocodile", "C.Elephant", " D.Ostrich"), 
# #            ("A.Nitrogen", " B.Oxygen", "C.Carbon-Dioxide", " D.Hydrogen"),
# #            ("A.206", " B.207", "C.208", " D.209"),
# #            ("A.Mercury", " B.Venus", "C.Earth", " D.Mars"))

# # answers = ("C", "D", "A","A","B")
# # guesses = []
# # score = 0
# # question_num = 0 

# # for question in questions:
# #     print("--------------------")
# #     print(question)
    
# #     for option in  options[question_num]:
# #         print(option)
        
# #         guess = input("Enter (A,B,C,D):").upper()
# #         guesses.append(guesses)
# #         if guess == answers[question_num]:
# #             score +=1
# #             print("CORRECT!")
# #         else:
# #             print("INCORRECT!")
# #             print(f"{answers[question_num]} is the correcy answer")
# #         question_num +=1

# # print("--------------------")
# # print("      RESULTS    ")
# # print("-----------------------")
# # print("answers:",end="")
# # for answer in answers:
# #     print(answer, end=" ")
# #     print()
    
# #     print("guesses:",end="")
# #     for guess in guesses:
# #         print(guess, end=" ")
# #         print()

# # score = int(score / len(questions)*100)
# # print(f"Your score is : {score}%")





# #9.Concession stand program
# # menu = {"pizza": 3.00,
# #         "nachos": 4.50,
# #         "popcorn": 6.00,
# #         "fries": 2.50,
# #         "chips": 1.00,
# #         "pretzel": 3.50,
# #         "soda":3.00,
# #         "lemonade": 4.25}

# # cart = []
# # total = 0
# # print("---------------MENU --------------")
# # for key,value in menu.items():
# #     print(f"{key:10}: ${value:.2f}")

# # print("-------------------------")

# # while True:
# #     food = input("Select an item (q to quit):").lower()
# #     if food == "q":
# #         break
    
# #     elif menu.get(food) is not None:
# #         cart.append(food)
# # print("------ YOUR ORDER--------")
        
# # for food in cart:
# #     total += total + menu.get(food)
# #     print(food, end=" ")        
        
# # print() 
# # print(f"Total is: ${total:.2f}")       



# #10.Python number guessing game
# # import random
# # lowest_num = 1
# # highest_num = 1000
# # answer = random.randint(lowest_num, highest_num)
# # guesses = 0
# # is_running = True

# # print("Python Number Guessing GAME")
# # print(f"Select a number between {lowest_num} and {highest_num}")        

# # while is_running:
# #     guess = input("Enter your guess:")  
    
# #     if guess.isdigit():
# #         guess = int(guess)
# #         guesses +=1
        
# #         if guess < lowest_num or guess > highest_num:
# #             print("That number is out of range")
# #             print(f"Please select a number between {lowest_num} and {highest_num}")
# #         elif guess < answer:
# #             print("Too low! Try again!")
# #         elif guess > answer:
# #             print("Too high! Try again!")
# #         else:
# #             print(f"CORRECT! The answer was {answer}")
# #             print(f"Number of guesses: {guesses}")
# #             is_running = False
            
        
# #     else:
# #         print("Invalid guess")
# #         print(f"Please select a number between {lowest_num} and {highest_num}")
         



# #11.rock,paper,scissors game
# # import random
# # options = ("rock", "paper", "scissors")
# # running = True

# # while running:
# #     player = None
# #     computer = random.choice(options)
    
# #     while player not in options:
# #         player = input("Enter a choice (rock,paper,scissors):")
        
# #         print(f"Player: {player}")
# #         print(f"Computer: {computer}")
        
# #         if player == computer:
# #             print("It's a tie!")
# #         elif player == "rock" and computer == "scissors":
# #             print("You win!")
# #         elif player == "paper" and computer == "rock":
# #             print("You win!")
# #         elif player == "scissors" and computer == "paper":
# #             print("You win!")
# #         else:
# #             print("You lose!")
            
# #             play_again = input("Play again? (y/n):") .lower()
# #             if not play_again == "y":
# #                 running = False
                
# # print("Thanks for playing!")
                
            


# #12.Dice roller program
# # import random

# # def roll_dice():
# #     return random.randint(1, 6)

# # def main():
# #     while True:
# #         input("Press Enter to roll the dice...")
# #         roll = roll_dice()
# #         print(f"You rolled a {roll}!")
        
# #         another_roll = input("Do you want to roll again? (y/n): ")
# #         if another_roll.lower() != 'y':
# #             break

# # if __name__ == "__main__":
# #     main()



# #13.encryption program
# # import random
# # import string

# # # Rastgele bir anahtar oluştur
# # def generate_key():
# #     characters = string.ascii_letters + string.digits + string.punctuation
# #     key = ''.join(random.sample(characters, len(characters)))
# #     return key

# # # Mesajı şifrele
# # def encrypt_message(message, key):
# #     encrypted_message = ''.join(key[string.ascii_letters.index(c)] if c in string.ascii_letters else c for c in message)
# #     return encrypted_message

# # # Mesajı deşifrele
# # def decrypt_message(encrypted_message, key):
# #     decrypted_message = ''.join(string.ascii_letters[key.index(c)] if c in key else c for c in encrypted_message)
# #     return decrypted_message

# # def main():
# #     # Anahtar oluştur
# #     key = generate_key()
# #     print(f"Generated Key: {key}")

# #     # Kullanıcıdan mesaj al
# #     message = input("Enter a message to encrypt: ")

# #     # Mesajı şifrele
# #     encrypted_message = encrypt_message(message, key)
# #     print(f"Encrypted message: {encrypted_message}")

# #     # Mesajı deşifrele
# #     decrypted_message = decrypt_message(encrypted_message, key)
# #     print(f"Decrypted message: {decrypted_message}")

# # if __name__ == "__main__":
# #     main()




# #14.Credit card validator

# # sum_of_digits = 0
# # sum_even_digits = 0
# # total = 0
# # # Step 1
# # card_number = input("ENTER a credit card #:")
# # card_number = card_number.replace("-", "")
# # card_number = card_number.replace(" ", "")
# # card_number = card_number [::-1]
# # # Step2
# # for x in card_number[::2]:
# #       sum_of_digits +=int(x)


# # #Step3
# # for x in card_number[1::2]:
# #     x = int(x)*2
# #     if x >=10:
# #         sum_even_digits += (1+(x%10))
# #     else:
# #         sum_even_digits += x
        
        
# # #Step4
# # total = sum_of_digits + sum_even_digits

# # #Step5
# # if total % 10 == 0:
# #     print("VALID")
# # else:
# #     print("INVALID")




# #15.Banking program
# # def show_balance():
# #     print(f"Your balance is: ${balance:.2f}")

# # def deposit():
# #     try:
# #         amount = float(input("Enter an amount to be deposited: "))
# #         if amount < 0:
# #             print("That's not a valid amount.")
# #             return 0
# #         else:
# #             return amount
# #     except ValueError:
# #         print("Please enter a valid number.")
# #         return 0

# # def withdraw():
# #     try:
# #         amount = float(input("Enter an amount to be withdrawn: "))
# #         if amount < 0:
# #             print("That's not a valid amount.")
# #             return 0
# #         elif amount > balance:
# #             print("Insufficient funds.")
# #             return 0
# #         else:
# #             return amount
# #     except ValueError:
# #         print("Please enter a valid number.")
# #         return 0

# # balance = 0
# # is_running = True

# # while is_running:
# #     print("\nBanking program")
# #     print("1. Show Balance")
# #     print("2. Deposit")
# #     print("3. Withdraw")
# #     print("4. Exit")
    
# #     choice = input("Enter your choice (1-4): ")
# #     if choice == "1":
# #         show_balance()
# #     elif choice == "2":
# #         balance += deposit()
# #     elif choice == "3":
# #         balance -= withdraw()
# #     elif choice == "4":
# #         is_running = False
# #     else:
# #         print("That is not a valid choice!")

# # print("Thank you, have a nice day!")





# #16.Slot machine
# # import random

# # def spin_slot_machine():
# #     symbols = ["🍒", "🍋", "🍊", "🍏", "🍉", "⭐"]
# #     return random.choices(symbols, k=3)

# # def check_win(spin_result):
# #     return spin_result[0] == spin_result[1] == spin_result[2]

# # def main():
# #     balance = 100  # Starting balance
# #     print("Welcome to the Slot Machine!")
    
# #     while True:
# #         print(f"Your balance: ${balance}")
# #         play = input("Press 'Enter' to spin or 'q' to quit: ")
        
# #         if play.lower() == 'q':
# #             print("Thank you for playing! Goodbye!")
# #             break
        
# #         spin_result = spin_slot_machine()
# #         print("🎰 " + " | ".join(spin_result) + " 🎰")
        
# #         if check_win(spin_result):
# #             print("Congratulations! You win!")
# #             balance += 10  # Win amount
# #         else:
# #             print("Sorry, you lose.")
# #             balance -= 5  # Lose amount
        
# #         if balance <= 0:
# #             print("You're out of money! Game over.")
# #             break

# # if __name__ == "__main__":
# #     main()






# #17.Hangman game:
# # import random

# # def choose_word():
# #     words = ["python", "hangman", "programming", "challenge", "computer", "science"]
# #     return random.choice(words)

# # def display_hangman(tries):
# #     stages = [
# #         """
# #            ------
# #            |    |
# #            |    O
# #            |   /|\\
# #            |   / \\
# #            |
# #         """,
# #         """
# #            ------
# #            |    |
# #            |    O
# #            |   /|\\
# #            |   /
# #            |
# #         """,
# #         """
# #            ------
# #            |    |
# #            |    O
# #            |   /|
# #            |
# #            |
# #         """,
# #         """
# #            ------
# #            |    |
# #            |    O
# #            |    |
# #            |
# #            |
# #         """,
# #         """
# #            ------
# #            |    |
# #            |    O
# #            |
# #            |
# #            |
# #         """,
# #         """
# #            ------
# #            |    |
# #            |
# #            |
# #            |
# #            |
# #         """,
# #         """
# #            ------
# #            |
# #            |
# #            |
# #            |
# #            |
# #         """
# #     ]
# #     return stages[tries]

# # def play_hangman():
# #     word = choose_word()
# #     guessed_letters = []
# #     tries = 6
# #     word_completion = "_" * len(word)

# #     print("Welcome to Hangman!")
# #     print(display_hangman(tries))
# #     print(word_completion)
    
# #     while tries > 0 and "_" in word_completion:
# #         guess = input("Guess a letter: ").lower()

# #         if len(guess) != 1 or not guess.isalpha():
# #             print("Invalid input. Please enter a single letter.")
# #             continue
        
# #         if guess in guessed_letters:
# #             print("You already guessed that letter. Try again.")
# #             continue
        
# #         guessed_letters.append(guess)

# #         if guess in word:
# #             print(f"Good guess! '{guess}' is in the word.")
# #             word_completion = "".join(
# #                 [letter if letter in guessed_letters else "_" for letter in word]
# #             )
# #         else:
# #             print(f"Sorry, '{guess}' is not in the word.")
# #             tries -= 1

# #         print(display_hangman(tries))
# #         print(word_completion)

# #     if "_" not in word_completion:
# #         print("Congratulations, you guessed the word!")
# #     else:
# #         print(f"Sorry, you're out of tries. The word was '{word}'.")

# # if __name__ == "__main__":
# #     play_hangman()





# # #18.Alarm Clock
# # import time
# # import winsound  # For Windows sound; use `os` for other OSs

# # def set_alarm(alarm_time):
# #     print(f"Alarm set for {alarm_time}.")
# #     while True:
# #         time.sleep(1)  # Check every second
# #         current_time = time.strftime("%H:%M")
# #         if current_time == alarm_time:
# #             print("Time to wake up!")
# #             # Play sound (Windows)
# #             winsound.Beep(440, 1000)  # Frequency 440Hz for 1 second
# #             break

# # def main():
# #     print("Welcome to the Alarm Clock!")
# #     alarm_time = input("Enter the time for the alarm (HH:MM, 24-hour format): ")
    
# #     try:
# #         time.strptime(alarm_time, "%H:%M")  # Validate time format
# #         set_alarm(alarm_time)
# #     except ValueError:
# #         print("Invalid time format. Please enter time in HH:MM format.")

# # if __name__ == "__main__":
# #     main()




# #19.Digital Clock
# # import tkinter as tk
# # import time

# # def update_time():
# #     current_time = time.strftime("%H:%M:%S")
# #     clock_label.config(text=current_time)
# #     clock_label.after(1000, update_time)  # Update every 1000 ms (1 second)

# # # Set up the main window
# # root = tk.Tk()
# # root.title("Digital Clock")

# # # Create a label to display the time
# # clock_label = tk.Label(root, font=("Helvetica", 48), fg="black")
# # clock_label.pack()

# # # Start the clock
# # update_time()

# # # Run the application
# # root.mainloop()



# #20.StopWatch
# # import tkinter as tk

# # class Stopwatch:
# #     def __init__(self, master):
# #         self.master = master
# #         self.master.title("Stopwatch")

# #         self.is_running = False
# #         self.time_elapsed = 0

# #         self.label = tk.Label(master, text="00:00:00", font=("Helvetica", 48))
# #         self.label.pack()

# #         self.start_button = tk.Button(master, text="Start", command=self.start)
# #         self.start_button.pack(side=tk.LEFT)

# #         self.stop_button = tk.Button(master, text="Stop", command=self.stop)
# #         self.stop_button.pack(side=tk.LEFT)

# #         self.reset_button = tk.Button(master, text="Reset", command=self.reset)
# #         self.reset_button.pack(side=tk.LEFT)

# #     def start(self):
# #         if not self.is_running:
# #             self.is_running = True
# #             self.update_time()

# #     def stop(self):
# #         self.is_running = False

# #     def reset(self):
# #         self.stop()
# #         self.time_elapsed = 0
# #         self.label.config(text="00:00:00")

# #     def update_time(self):
# #         if self.is_running:
# #             self.time_elapsed += 1
# #             hours, remainder = divmod(self.time_elapsed, 3600)
# #             minutes, seconds = divmod(remainder, 60)
# #             time_string = f"{hours:02}:{minutes:02}:{seconds:02}"
# #             self.label.config(text=time_string)
# #             self.master.after(1000, self.update_time)

# # if __name__ == "__main__":
# #     root = tk.Tk()
# #     stopwatch = Stopwatch(root)
# #     root.mainloop()



# # BRO CODE YOUTUBE FINISH



# # freeCodeCamp.org YOUTUBE START
# #1.Madlibs
# # youtuber = "Kylie Ying"
# # print("subscribe to" + youtuber)
# # print("subscribe to {}".format(youtuber))
# # print(f"subscribe to {youtuber}")

# # adj = input("Adjective:")
# # verb1 = input("Verb:")
# # verb2 = input("Verb:")
# # famous_person = input("Famous person:")
# # madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
# #     I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

# # print(madlib)



# #2.Guess the Number(Computer)
# # import random

# # # Kullanıcının tahmin etmesini sağlayan fonksiyon
# # def user_guess(x):
# #     random_number = random.randint(1, x)
# #     guess = 0
    
# #     while guess != random_number:
# #         try:
# #             guess = int(input(f'1 ile {x} arasında bir sayı tahmin et: '))
# #             if guess < random_number:
# #                 print('Üzgünüm, tahminin çok düşük.')
# #             elif guess > random_number:
# #                 print('Üzgünüm, tahminin çok yüksek.')
# #         except ValueError:
# #             print("Lütfen geçerli bir tam sayı girin.")
    
# #     print(f'Tebrikler! {random_number} sayısını doğru tahmin ettin.')

# # # Bilgisayarın tahmin etmesini sağlayan fonksiyon
# # def computer_guess(x):
# #     low = 1
# #     high = x
# #     feedback = ''
    
# #     while feedback != 'c':
# #         guess = random.randint(low, high)
# #         feedback = input(f"Bilgisayarın tahmini: {guess}. Bu tahmin (H) çok yüksek, (L) çok düşük veya (C) doğru mu? ").lower()
        
# #         if feedback == 'h':
# #             high = guess - 1
# #         elif feedback == 'l':
# #             low = guess + 1
# #         elif feedback == 'c':
# #             print(f'Bilgisayar {guess} sayısını doğru tahmin etti!')
# #         else:
# #             print("Lütfen geçerli bir geri bildirim verin (H, L, C).")

# # # Oyunu başlat
# # print("Kullanıcı Tahmini Oyunu")
# # user_guess(10)

# # print("\nBilgisayar Tahmini Oyunu")
# # computer_guess(10)



# #4.Rock Paper scissors
# # import random

# # def is_win(player, opponent):
# #     # Oyuncunun kazanıp kazanmadığını kontrol et
# #     return (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r')

# # def play():
# #     user = input("'r' for rock, 'p' for paper, 's' for scissors: ")
# #     computer = random.choice(['r', 'p', 's'])

# #     print(f"Computer chose: {computer}")

# #     if user == computer:
# #         return "It's a tie!"
    
# #     if is_win(user, computer):
# #         return "You won!"
    
# #     return "You lost!"

# # # Oyunu başlat
# # if __name__ == "__main__":
# #     print(play())


# #5.Hangman Game
# # import random

# # def hangman():
# #     word_list = ["python", "hangman", "programming", "developer", "code", "computer"]
# #     word = random.choice(word_list)
# #     guessed = "_" * len(word)
# #     guessed_list = list(guessed)
# #     attempts = 6
# #     guessed_letters = []

# #     print("Welcome to Hangman!")
    
# #     while attempts > 0 and "_" in guessed_list:
# #         print("\nCurrent word: " + " ".join(guessed_list))
# #         print(f"Attempts remaining: {attempts}")
# #         print("Guessed letters: " + ", ".join(guessed_letters))
        
# #         guess = input("Guess a letter: ").lower()
        
# #         if len(guess) != 1 or not guess.isalpha():
# #             print("Please enter a single letter.")
# #             continue
        
# #         if guess in guessed_letters:
# #             print("You already guessed that letter.")
# #             continue
        
# #         guessed_letters.append(guess)
        
# #         if guess in word:
# #             for index, letter in enumerate(word):
# #                 if letter == guess:
# #                     guessed_list[index] = guess
# #             print("Good guess!")
# #         else:
# #             attempts -= 1
# #             print("Wrong guess!")
        
# #     if "_" not in guessed_list:
# #         print("\nCongratulations! You've guessed the word: " + word)
# #     else:
# #         print("\nSorry, you ran out of attempts. The word was: " + word)

# # if __name__ == "__main__":
# #     hangman()



# #6.Tic-Tac-Toe
# # class TicTacToe:
# #     def __init__(self):
# #         self.board = [' ' for _ in range(9)]  # 3x3 board
# #         self.current_winner = None  # Keep track of the winner

# #     def print_board(self):
# #         for row in [self.board[i * 3: (i + 1) * 3] for i in range(3)]:
# #             print('I' + 'I'.join(row) + 'I')

# #     @staticmethod
# #     def print_board_nums():
# #         number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
# #         for row in number_board:
# #             print("I" + 'I'.join(row) + 'I')

# #     def available_moves(self):
# #         return [i for i, spot in enumerate(self.board) if spot == ' ']

# #     def empty_squares(self):
# #         return ' ' in self.board

# #     def num_empty_squares(self):
# #         return self.board.count(' ')

# #     def make_move(self, square, letter):
# #         if self.board[square] == ' ':
# #             self.board[square] = letter
# #             if self.winner(square, letter):
# #                 self.current_winner = letter  # Set the winner
# #             return True
# #         return False

# #     def winner(self, square, letter):
# #         # Check the row
# #         row_ind = square // 3
# #         if all(self.board[row_ind * 3 + i] == letter for i in range(3)):
# #             return True
# #         # Check the column
# #         col_ind = square % 3
# #         if all(self.board[col_ind + i * 3] == letter for i in range(3)):
# #             return True
# #         # Check diagonals
# #         if square % 2 == 0:  # square is even
# #             if all(self.board[i] == letter for i in [0, 4, 8]):
# #                 return True
# #             if all(self.board[i] == letter for i in [2, 4, 6]):
# #                 return True
# #         return False

# # def play(game, x_player, o_player, print_game=True):
# #     if print_game:
# #         game.print_board_nums()

# #     letter = 'X'  # Starting letter
# #     while game.empty_squares():
# #         if letter == 'O':
# #             square = o_player.get_move(game)
# #         else:
# #             square = x_player.get_move(game)

# #         if game.make_move(square, letter):
# #             if print_game:
# #                 print(letter + f' makes a move to square {square}')
# #                 game.print_board()

# #             if game.current_winner:
# #                 print(letter + ' wins!')
# #                 return
# #             letter = 'O' if letter == 'X' else 'X'  # Switch turns

# #     print('It\'s a tie!')

# # # Example player classes
# # class HumanPlayer:
# #     def get_move(self, game):
# #         valid_square = False
# #         value = None
# #         while not valid_square:
# #             square = input('Enter your move (0-8): ')
# #             try:
# #                 value = int(square)
# #                 if value in game.available_moves():
# #                     valid_square = True
# #                 else:
# #                     print('Invalid square. Try again.')
# #             except ValueError:
# #                 print('Invalid input. Enter a number between 0 and 8.')
# #         return value

# # # Example usage
# # if __name__ == '__main__':
# #     x_player = HumanPlayer()
# #     o_player = HumanPlayer()  # You can replace this with another player type
# #     t = TicTacToe()
# #     play(t, x_player, o_player)

            


# #8.Binary Search
# # def naive_search(l, target):
# #     for i in range(len(l)):
# #         if l[i] == target:
# #             return i
# #     return -1  # Moved outside the loop

# # def binary_search(l, target, low=None, high=None):
# #     if low is None:
# #         low = 0
# #     if high is None:
# #         high = len(l) - 1

# #     if high < low:
# #         return -1

# #     midpoint = (low + high) // 2

# #     if l[midpoint] == target:
# #         return midpoint
# #     elif target < l[midpoint]:
# #         return binary_search(l, target, low, midpoint - 1)  # Added low and high
# #     else:
# #         return binary_search(l, target, midpoint + 1, high)  # Added low and high

# # if __name__ == '__main__':
# #     l = [1, 3, 5, 10, 12]
# #     target = 10
# #     print(naive_search(l, target))  # Should print index of target
# #     print(binary_search(l, target))  # Should print index of target





# #9.MinesWeeper
# # import random

# # class Minesweeper:
# #     def __init__(self, width, height, num_mines):
# #         self.width = width
# #         self.height = height
# #         self.num_mines = num_mines
# #         self.board = [[' ' for _ in range(width)] for _ in range(height)]
# #         self.visible = [[' ' for _ in range(width)] for _ in range(height)]
# #         self.game_over = False
# #         self._place_mines()
# #         self._calculate_numbers()

# #     def _place_mines(self):
# #         placed_mines = 0
# #         while placed_mines < self.num_mines:
# #             x = random.randint(0, self.width - 1)
# #             y = random.randint(0, self.height - 1)
# #             if self.board[y][x] != '*':
# #                 self.board[y][x] = '*'
# #                 placed_mines += 1

# #     def _calculate_numbers(self):
# #         for y in range(self.height):
# #             for x in range(self.width):
# #                 if self.board[y][x] == '*':
# #                     continue
# #                 # Count surrounding mines
# #                 count = sum(
# #                     1 for dy in range(-1, 2) for dx in range(-1, 2)
# #                     if 0 <= x + dx < self.width and 0 <= y + dy < self.height
# #                     and self.board[y + dy][x + dx] == '*'
# #                 )
# #                 self.board[y][x] = str(count) if count > 0 else ' '

# #     def display(self):
# #         print("   " + " ".join(str(x) for x in range(self.width)))
# #         for y in range(self.height):
# #             print(f"{y} | " + " ".join(self.visible[y]))
# #         print()

# #     def reveal(self, x, y):
# #         if self.board[y][x] == '*':
# #             self.game_over = True
# #             return
# #         self._reveal_recursive(x, y)

# #     def _reveal_recursive(self, x, y):
# #         if self.visible[y][x] != ' ':
# #             return
# #         self.visible[y][x] = self.board[y][x]
# #         if self.board[y][x] == ' ':
# #             for dy in range(-1, 2):
# #                 for dx in range(-1, 2):
# #                     if 0 <= x + dx < self.width and 0 <= y + dy < self.height:
# #                         self._reveal_recursive(x + dx, y + dy)

# #     def play(self):
# #         while not self.game_over:
# #             self.display()
# #             x = int(input("Enter x coordinate (0 to {}): ".format(self.width - 1)))
# #             y = int(input("Enter y coordinate (0 to {}): ".format(self.height - 1)))
# #             if 0 <= x < self.width and 0 <= y < self.height:
# #                 self.reveal(x, y)
# #             else:
# #                 print("Invalid coordinates! Please try again.")

# #         print("Game Over!")
# #         self.display()

# # if __name__ == "__main__":
# #     width = 10
# #     height = 10
# #     num_mines = 10
# #     game = Minesweeper(width, height, num_mines)
# #     game.play()



# #10.Sudoku Solver
# # def print_board(board):
# #     for row in board:
# #         print(" ".join(str(num) for num in row))

# # def find_empty(board):
# #     for r in range(9):
# #         for c in range(9):
# #             if board[r][c] == 0:  # 0 represents an empty cell
# #                 return r, c  # Return the row and column of the empty cell
# #     return None  # No empty cell found

# # def is_valid(board, guess, row, col):
# #     # Check row
# #     if guess in board[row]:
# #         return False
    
# #     # Check column
# #     if guess in (board[r][col] for r in range(9)):
# #         return False
    
# #     # Check 3x3 square
# #     row_start = (row // 3) * 3
# #     col_start = (col // 3) * 3
# #     for r in range(row_start, row_start + 3):
# #         for c in range(col_start, col_start + 3):
# #             if board[r][c] == guess:
# #                 return False
    
# #     return True

# # def solve_sudoku(board):
# #     empty = find_empty(board)
# #     if not empty:
# #         return True  # Solved

# #     row, col = empty
    
# #     for guess in range(1, 10):  # Numbers 1-9
# #         if is_valid(board, guess, row, col):
# #             board[row][col] = guess  # Place the guess
            
# #             if solve_sudoku(board):
# #                 return True  # Solved
            
# #             board[row][col] = 0  # Reset (backtrack)
    
# #     return False  # Trigger backtracking

# # if __name__ == "__main__":
# #     sudoku_board = [
# #         [5, 3, 0, 0, 7, 0, 0, 0, 0],
# #         [6, 0, 0, 1, 9, 5, 0, 0, 0],
# #         [0, 9, 8, 0, 0, 0, 0, 6, 0],
# #         [8, 0, 0, 0, 6, 0, 0, 0, 3],
# #         [4, 0, 0, 8, 0, 3, 0, 0, 1],
# #         [7, 0, 0, 0, 2, 0, 0, 0, 6],
# #         [0, 6, 0, 0, 0, 0, 2, 8, 0],
# #         [0, 0, 0, 4, 1, 9, 0, 0, 5],
# #         [0, 0, 0, 0, 8, 0, 0, 7, 9]
# #     ]

# #     print("Original Sudoku Board:")
# #     print_board(sudoku_board)
    
# #     if solve_sudoku(sudoku_board):
# #         print("\nSolved Sudoku Board:")
# #         print_board(sudoku_board)
# #     else:
# #         print("No solution exists.")






# # Finish

# WsCube Tech 100+Python Programs with Practicals for Beginners:Start
# # num1 = 30
# # num2 = 40
# # sum = num1+num2
# # print("The sum of given two number is",sum )

# # num1 = float(input("enter a number here:"))
# # num2 = float(input("enter another number here:"))
# # sum = num1+num2
# # print("the sum of the provided two numbers is ", sum)



# print("hello world")



#Find the square root
# num = 64
# sr = num**(1/2)
# num1 = int(input("enter a number here: "))
# print("the square root of the given number is", sr)


#Using Math Module
# import math
# num = int(input("enter a number here: "))
# sr = math.sqrt(num)
# print("the square root of the given number is", sr)




#Calculate the Area of a Triagle
# height = float(input("enter the height of the triange: ")) 
# base = float(input("enter the base of the triangle: "))
# area = (0.5)*base*height
# print("the area of triangle is",area)



#Python program To selve Quadratic Equation
# import cmath
# a = int(input("enter number(a!=0):"))
# b = int(input("enter number: "))
# c = int(input("enter number: "))
# d = (b**2) - (4*a*c)
# root1 = (-b-cmath.sqrt(d)) / (2*a)
# root2 = (-b+cmath.sqrt(d)) / (2*a)
# print("the roots are", root1, "and", root2)




# Python Program to Swap
# x = 13
# y = 12
# temp = x
# print ("the value of temp variable is", temp)
# x = y
# print("the value of  x is",x)
# y = temp
# print("the value of y is",y)



# # Solution2
# x = 12
# y = 13
# x,y = y,x
# print("the value of x is", x)
# print("the value of y is", y)





# Python Program to Generate Random Number
# import random
# num = random.randint(0,10)
# print(num)


# Python Program to Convert Kilometers to Miles
# km = float(input("enter your value in kms: "))
# miles = (0.0621371)*km
# print(km, "kms in miles will be ", miles, "miles")



#Python to Convert Celsius to Fahreneit
# celsius = int(input("enter temperature in celsius:"))
# fahreneit = (celsius * (9/5))+32
# print("the converted value is", fahreneit, "Fahreneit")



#Check if a Number is Positive,Negative or 0
# num = 12
# if num>0:
#     print("It is a positive number")
# elif num == 0:
#     print("it is zero")
# else:
#     print("It is a negative number")
    
    
    
# Check if a Number is Odd or Even
# num = int(input("enter a number here: "))
# if num % 2 == 0:
#     print("It is an even number ")
# else:
#     print("It is an odd number")
    



# Check Leap Year
# year = int(input("enter a year: "))
# if (year % 400 == 0) and (year % 100 == 0):
#     print(year, "is a leap year")
# elif (year % 4 == 0) and (year % 100 !=0):
#     print(year, "is a leep year")
# else:
#     print(year, "is not a leap year")
    
    
    
# Find the Largest Among Three Numbers
# num1 = int(input('enter 1st number here: '))
# num2 = int(input("enter 2nd number here: "))
# num3 = int(input("enter 3rd number here: "))
# if (num1>num2) and (num1> num3):
#     print(num1, "is the largest number")
# elif(num2>num1) and (num2>num3):
#     print(num2, "is the largest number")
# else:
#     print(num3, "is the largest number")
    


#Print all Prime Numbers in an Interval
# lower = int(input("enter lower limit here:"))
# upper = int(input("enter upper limit here: "))
# for num in range(lower, upper + 1):
#     if num > 1:
#         for i in range(2,num):
#             if num %i == 0:
#                 break
#             else:
#                 print(num)



#Factorial Number:
# def fact(a):
#     if a == 0 :
#         return 1
#     else:
#         return ((a)*fact(a-1))
    
# num = int(input("enter a number here: "))
# result = fact(num)
# print("The factorial of the given number is", result)





# Display the multiplication Table:
# Solution 1 With for Loop
# n = int(input('enter a number here: '))
# for i in range(1,11):
#     print(n, "x", i, "=", n*i)


# Solution 2 While Loop
# n = 7
# i = 1
# while i<=10:
#     print(n, "x", i, "=", n*i)
#     i +=1
    



# Fibonacci sequence:
# a = 0
# b = 1
# num = int(input("enter a number to obtain fibonacci sequence: "))
# if num == 1:
#     print(a)
# else:
#     print(a)
#     print(b)
#     for i in range (1,num+1):
#         c = a+b
#         a = b
#         b = c
#         print(c)






# Check Armstrong Number:
# num = int(input('enter a number here: '))
# order = len(str(num))
# sum = 0
# temp = num
# while temp > 0:
#     digit = temp%10
#     sum += digit **order
#     temp //=10


# if sum == num:
#     print("it is an armstrong number")
# else:
#     print("it is not arm")




#  Amstrong Number in an Interval:
# lower = int(input("enter the lower limit here:"))
# upper = int(input("enter the upper limit here: "))
# sum = 0
# for num in range(lower, upper + 1):
#     order = len(str(num))
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         sum += digit **order
#         temp //=10
#         if num == sum:
#             print(num)
            
            
            

# Python Program to Find the Sum of Natural Numbers:
# num = int(input('enter a number here: '))
# if num < 0:
#     print('please enter positive number')
# else:
#     sum = 0
#     while num >0:
#         sum +=num
#         num -=1
        
#         print(sum)




# Python Program to Display Powers of 2 Using Anonymous Function:
# nterms = int(input("enter a number of terms here: "))
# result = list(map(lambda x : 2 **x, range(nterms +1)))
# print(result)
# for i in range(nterms+1):
#     print("the value of 2 raised to power", i, "is", result[i])



#Find Numbers Divisible by Another Number:
#Solution 1 Using for Loop
# print("The numbers divisible by 13 are:")
# for i in range(1,100):
#     if i % 13 == 0:
#         print(i)


#Solution 2: Using Lambda & Filter() Function()
# l = [39,48,26,98,33,67,87]
# result = list(filter(lambda x: x%13 == 0,l))
# print('the numbers divisible by 13 are', result)




# Convert Decimal to Binary,Octal and Hexadecimal
#Solution (Binary, Octal And Hexadecimal)
# decimal = int(input('enter a number here: '))
# print('the conversion of decimal number', decimal, "is:")
# print(bin(decimal), "in binary")
# print(oct(decimal), "in octal")
# print(hex(decimal), "in hexadecimal")



#Find ACII Value of Character:
# char = "a"
# print("the ASCII value of", char, "is", ord(char))




# Find HCF or GCD:
# def findHCF(x,y):
#     if x > y:
#         smaller = y
#     else:
#         smaller = x
#         for i in range(1,smaller+1):
#             if ((x%i == 0) and (y % i == 0)):
#                 hcf = i
#                 return hcf
            
# print("the hcf of the given two number two numbers is", findHCF(12,30))




# Factors of a Number:
# num = int(input('enter a number here: '))
# for i in range(1,num +1):
#     if num % i == 0:
#         print(i)



# Make a Simple Calculator:
# print("~~~~~~~~~~Mini Calculator~~~~~~~~~~")
# num1 = float(input("enter a number here:"))
# num2 = float(input("enter second number here: "))
# print("press 1 for addition \npress 2 for substraction \npress 3 for multiplication \npress 4 for division")

# choice = int(input("enter your choice from 1-4: "))
# if choice == 1:
#     print(num1+num2)
# elif choice == 2:
#     print(num1-num2)
# elif choice == 3:
#     print(num1*num2)
# elif choice == 4:
#     print(num1 / num2)
# else:
#     print("Invalid Input")




# Shuffle Deck of Cards
# import random, itertools
# deck = list(itertools.product(range(1,14), ["Spade", "Club", "Hearts", "Diamond"]))
# random.shuffle(deck)
# print(deck)
# for i in range(5):
#     print(deck[i][0], "of", deck[i][1])



# Display Calendar:
# import calendar
# year = int(input("enter year:"))
# month = int(input("enter month:"))
# calendar = calendar.month(year,month)
# print(calendar)




# Display Fibonacci Sequence Using Recursion
# def fibo(n):
#     if n <=1:
#         return n
    
#     else:
#         return fibo(n-1)+fibo(n-2)

# n = int(input("enter a number here:"))  
# if n <=0:
#     print("enter a positive number")
# else:
#     print("fibonacci sequence")
#     for i in range(n):
#         print(fibo(i))
    



#Find Sum of Natural Numbers Using Recursion
# def NNS(n):
#     if n <=1:
#         return n
#     else:
#         return (n)+NNS(n-1)
    
    
# n = int(input("enter a number here: "))
# if n <=0:
#     print("enter a positive number")
# else:
#     print("The sum of natural number upto given number is", NNS(n))
    
    

# Find Factorial of Number Using Recursion
# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return (n*fact(n-1))
    

# n = int(input('enter a number here:'))
# if n <=0:
#     print('Factorial of number less than 1 does not exists')
# else:
#     print("Factorial of given number is", fact(n))
    
    
    
# Convert Decimal to Binary Using Recursion
# def ConvertBinary(n):
#     if n >1:
#         ConvertBinary(n//2)
        
#         print(n%2, end=" ")

# print("the binary of the given number is:")        
# ConvertBinary(15)




# Add Two Matrices
# A = [[1,5,8],
#      [4,6,7],
#      [7,2,3]],

# B = [[4,5,6],
#      [8,9,1],
#      [3,5,6]],

# result = [[0,0,0],
#           [0,0,0],
#           [0,0,0]],

# for i in range(len(A)):
#     for j in range(len(A[0])):
#         result [i][j] = A[i][j] + B [i][j]
        
# print(result)




# Transpose a Matrix:
# A = [[1,2,3],
#      [4,5,6]]

# T = [A[j][i] for j in range(len(A)) for i in range(len(A[0]))]
# for i in T:
#     print(i)



# Multiply Two Matrices
# A = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]

# B = [[1,2,1,1],
#      [4,2,1,2],
#      [6,3,4,1]]

# result = [[0,0,0,0],
#           [0,0,0,0],
#           [0,0,0,0]]


# for i in range(len(A)):
#     for j in range(len(B[0])):
#         for k in range(len(B)):
#             result [i][j] += A[i][k] *B[k][j]
            
# for i in result:
#     print(result)




# Check Whether a String is Palindrome or Not:
# a = input("Enter a word here:")
# rev = a[::-1]

# if a == rev:
#     print("It is a palindrome ")
# else:
#     print("It is not palindrome")




# Remove Punctuations From a String
# punc = ''''!()-[]{};: \, /?@#$%^&*_~'''
# string = input("enter anything here: ")
# empty_str = ""
# for i in string:
#     if i not in punc:
#         empty_str +=i
        
# print(empty_str)



# Sort words in Alphabetic Order
# a = input('enter something here: ')
# w = a.split()
# print(w)
# for i in range(len(w)):
#     w[i] = w[i].lower()
    
#     print(w)
#     w.sort()
#     print(w)
#     for i in w:
#         print(i)




# Different Set Operations
# A = [1,2,3,4,5,6,7,8,9]
# B = [3,4,5,6,7,8]
# print("The Union is", A / B)
# print("The Intersection is", A & B)
# print("The Difference is", A-B)
# print("The Symmetric difference is", A^B)




# Count the Number of Each Vowel
# a = "Harry Potter and Prisoner of Azkaban"
# vowels = "aeiou"
# a = a.casefold()
# print(a)
# count = {}.fromkeys(vowels,0)

# for char in a:
#     if char in count:
#         count[char]+=1
        
# print(count)


# Merge Two Dictionaries
# # Solution 1 Using / Operator
# dict1 = {"John": 89, "Lisa": 99}
# dict2 = {"Lisa": 94, "Peter": 78}
# print(dict1 | dict2)


# Solution 2 Using ** Operator
# dict1 = {"John": 89, "Lisa": 99}
# dict2 = {"Lisa": 94, "Peter": 78}
# print({**dict1, **dict2})
# dict3 = dict2.copy()
# dict3.update(dict1)
# print(dict3)



# Access Index of a List Using for Loop
# l = [34,5,61,54,89]
# for index , value in enumerate(l):
#     print(index,value)


# l = [34,5,61,54,89]
# for index in range(len(l)):
#     value = l[index]
#     print(index,value) 



# Python program to Slice Lists
# a = ["Joe", "Rachel", "Monica", "Phoebe", "Ross", "Chandler"]
# print(a[-6:-3])
# print(a[1:4])
# print(a[::])
# print(a[:3])
# print(a[2:])
# print(a[::2])
# print(a[::-1])



#Iterate Over Dictionaries Using For Loop
# friends = { "Rachel": "Rosss", "Monica": "Chandler", "Phoebe": "Joe"}
# print(friends)
# for key, value in friends.items():
#     print(key,value)
    

# for key in friends:
#     print(key)
    
    

# Python Program Sort a Dictionary by Value
# marks = {"John":23, "Lisa":56, "sid": 48}
# # print(marks)
# # sv = sorted(marks.items(), key = lambda x : x[1] )
# # print(sv)

# #Solution 2 (sort only the values)
# v = sorted(marks.values())
# print(v)



# Python Program to Check If a List is Empty
# Solution 1 using boolean operation
# my_list = []
# if not my_list:
#     print("The list is empty")


# my_list = []
# print(len(my_list))
# if len(my_list) == 0:
#     print("The list is empty")


# solution 3 using []
# my_list = []
# if my_list == []:
#     print("The list is empty")




# PYTHON PROGRAM TO CATCH MULTIPLE EXCEPTIONS IN ONE LINE:
# string = input("enter somthing here:")
# try:
#      num = int(input("enter a number here:"))
#      print(string+num)
     
# except (ValueError, TypeError) as a:
#     print(a)



# PYTHON PROGRAM TO CONCATENATE TWO LISTS
# Solution 1 Using + Operator
# l1 = [3,6,8,2, "a","j"]
# l2 = [3,6,"k", "f", "j"]
# l12 = l1+l2
# print(l12)


#Solution 2 with Unique Values
# l1 = [3,6,8,2,"a", "j"]
# l2 = [3,6,"k", "f", "j"]
# l12 = set(l1+l2)
# print(l12)



# PYTHON PROGRAM TO CHECK IF A KEY IS ALREADY PRESENT IN A DICTIONARY
# friends = {"Rachel": "Ross", "Monica": "Chandler", "Phoebe":"Joe" }
# name = "Monica"
# if name in friends.keys():
#     print("it is present")



#PYTHON PROGRAM TO PARSE A STRING TO A FLOAT OR INT
# string = "12345"
# print(type(string))
# int_str = int(string)
# print(type(int_str))


#Solution-2 (PARSE STRING INTO FLOAT)
# string = "123.45"
# print(type(string))
# float_string = float(string)
# print(type(float_string))


# Soltuion - 3: Parse string Float Numeral into Integer
# string = "123.45"
# print(type(string))
# str_float_int = float(string)
# print(type(str_float_int))



# PYTHON PROGRAM TO CONVERT STRING TO DATETIME
# from dateutil import parser
# date_time = parser.parse("Oct 14 1997 7:15 AM")
# print(date_time)
# print(type(date_time))



# PYTHON PROGRAM GET THE LAST ELEMENT OF THE LIST
# avengers = ["Ironman", "Hulk", "Thor", "Vision"]
# print(avengers[-1])


# PYTHON PROGRAM GET A SUBSTRING OF A STRING
# a = "Harry Potter and the Goblet of Fire"
# print(a[0:12])
# print(a[-14:])




# Python program to get the Last element of the List
# print("Harry potter", end=" ")
# print("and the Goblet of Fire")



# Python program Read a File Line by Line Into a List
# f = open("file.txt", "r")
# lines = f.readlines()
# print(lines)
# new_lines = [x.strip() for x in lines ]
# print(new_lines)


# f = open("file.txt", "r")
# line = [line for line in f]
# print(line)
# new_lines = [x.strip() for x in line]
# print(new_lines)




# Python Program to Randomly Select an Element From the List
# Solution(Select an element from list)
# num = input("enter something here: ")

# def float_check(num):
#     try:
#         float(num)
#         return True
#     except:
#         return False

# print(float_check(num))
    
    
    
# Python Program to check if a string is a number(float)
# import random
# l = [2,5,"a", "y", 8, "p"]
# random_value = random.choice(l)
# print(random_value)


# import secrets
# l = [2,5,"a", "y", 8, "p"]
# random_value = secrets.choice(l)
# print(random_value)




# Python Program to count the occurence of an item in a list
# numbers = [10,20,30,40,10,30,10,20,40,70]
# count_occurence = numbers.count(20)
# print(count_occurence)




# Python program to append to a file
# f = open("file.txt", "a")
# f.write("this is my demo file")
# f.close()



# Python program to delete an element from a dictionary
# marks = {"John":89, "Lisa":96, "David":65, "Petter":88}
# pop_item = marks.pop("John")
# print(marks)
# print(marks)
# del marks ["John"]
# print(marks)



#Python program to Create long Multiline String
# print("Hello everyone")
# print("this is my demo file")
# print("hope you all will like it")


# print("hello everyone \nthis is demo file \nI hope you all will like")

# string ="hello everyone \n"\
#     "this is my demo file\n"\
#         "hope you all will like it "
# print(string)



# Python Program to Extract extension from the file name
# import time
# starting_time = time.time()
# num = int(input("enter a number here: "))
# num1 = int(input("enter a number here: "))
# print(num+num1)
# ending_time = time.time()
# print(ending_time-starting_time)


# from timeit import default_timer as timer 
# starting_value = timer()
# print("hello world")
# ending_value = timer()
# print(ending_value - starting_value)



# Python program to get the class Name of an Instance
# class SmartPhone:
#     def name (self,name):
#         return name

# s1 = SmartPhone()
# print(s1.__class__.__name__)


# class SmartPhone:
#     def name(self,name):
#         return name
    
# s1 = SmartPhone
# print(type(s1).__name__)




# Python Program to Convert two Lists into a Dictionary
# name = ["John", "Peter", "Lisa", "David"]
# marks = [98,78,88,72]
# dictionary = zip(name, marks)
# print(tuple(dictionary))



# name = ["John", "Peter", "Lisa", "David"]
# marks = [98,78,88,72]
# dictionary = {key:value for key,value in zip(name,marks)}
# print(dictionary)




#Python program to differentiate between type() and isinstance()
# class SmartPhone:
#     def name(self):
#         pass
    
# class Nokia(SmartPhone):
#     def phone_name(self):
#         pass
    
# obj_SP = SmartPhone()
# obj_N  = Nokia()
# print(type(obj_SP)== SmartPhone)
# print(type(obj_N)== Nokia)


# print(isinstance(obj_SP, SmartPhone))
# print(isinstance(obj_N, Nokia))




# Python program to trim whitespace from a string
# string = "I love Python"
# print(string)
# print(string.strip())


# import re
# string = "  I love python"
# x = re.sub(r'^\s|\s$', '',string)
# print(x)



# Python Program to Represent enum
# from enum import Enum
# class SmartPhones(Enum):
#     Samsung = 1
#     Nokia = 2
#     Apple = 3
# print(SmartPhones.Samsung)    
# print(SmartPhones.Samsung.name)
# print(SmartPhones.Samsung.value)



# PYTHON PROGRAM TO RETURN MULTIPLE VALUES FROM A FUNCTION
# def friends():
#     return "Joe", "Pheobe"

# print(friends())
# n1, n2 = friends()
# print(n1,n2)


# def friends():
#     n1 = "Joe"
#     n2 = "Phoebe"
    
#     return {1 : n1 , 2: n2}

# print(friends())




# Python Program to Get Line Count of a File
# f = open("eli.txt", "r")
# print(len(f.readlines()))
# f.close()


# lines = sum(1 for i in open("eli.txt"))
# print(lines)


# Python program to Iterate through two lists in Parallel
# l1 = ["Rachel", "Monica", "Phoebe"]
# l2 = ["Ross", "Chandler", "Joe"]
# for x,y in zip (l1, l2):
#     print(x,y)



# Python Program to Reverse a Number
# num = int(input("enter a number here: "))
# reverse_num = 0
# while num != 0:
#     digit = num%10
#     reverse_num = reverse_num*10+ digit
#     num = num //10
    
# print(reverse_num)


# num = int(input("enter a number here:"))
# print(str(num)[::-1])



# Python program to compute the power of a Number
# base = int(input("Enter the base number: "))
# exponent = int(input("Enter the Exponent:"))
# result = 1
# while exponent != 0:
#     result = result*base
#     exponent = exponent -1
    
# print("The computed value is ", result)


# base = int(input("Enter the base number: "))
# exponent = int(input("Enter the Exponent:"))
# result = 1
# for i in range(exponent, 0,-1):
#     result = result *base
    
# print("The Computed value is", result)



# base = 2
# exponent = 5
# value = base**exponent
# print("The computed value is", value)




# Python Program to Count the Number of Digits present In a Number
# num = int(input("enter number a here: "))

# count = 0
# while num!= 0:
#     num = num //10
#     count = count +1
    
# print(count)



# num = 12345
# x = len(str(num))
# print(x)



# Python Program to Check if Two strings are Anagram
# a1 = "elbow"
# a2 = "below"
# if len(a1) == len(a2):
#     a1_sorted = sorted(a1)
#     a2_sorted = sorted(a2)
    
    
#     if a1_sorted == a2_sorted:
#         print("The string is an Anagram")
#     else:
#         print("The string is not an Anagram")
        
# else:
#     print("The string is not an Anigram")




# Python program to Capitalize the first character string
# a = "wscubetech"
# print(a.upper())

# a = "wscubetech"
# print(a.capitalize())



# Python program to create countdown Timer
# import time

# def countdown(sec):
#     while sec:
#         mins , secs = divmod(sec, 60)
#         time_format = "{:02d} : {:02d}".format(mins,secs)
#         print(time_format)
#         time.sleep(1)
#         sec -= sec -  1
#         print("Stop")

# countdown(5)



# Python Program to Count Number of Occurence of a Character in String
# string = "WsCubeTech"
# char = "e"
# count = 0
# for i in string:
#     if i == char:
#         count = count +1
        
# print(count)

# string = "wscubetech"
# char = "e"
# print(string.count(char))



# Remove Duplicate Element From a List
# l = [12,4,5,6,6,12,7,9,12]

# print(set(l))

# FINISH
