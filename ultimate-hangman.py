def hangman():
    from random import randint
    HANGMAN = (
"""
 -------------------------------------------------
|                    |
|                    |                      　　ゴ
|                    |                      
|           
|           　　　
|          
|        
|        
|     
|      
|                     
|         
|     
|     
|     
|        
|
|
|
|
|
|
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 _________________________________________________
 """
 ,
 """
 -------------------------------------------------
|                    |
|                    |                      　　ゴ
|                    |                      
|              ~~~~<[0]>~~~~              　　ゴ
|                   |||     　　　　　　　
|           
|      
|       
|      
|            
|               
|           
|                   
|             
|             
|                     
|            
|             
|             
|    
|
|
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 _________________________________________________
 """
 ,
 """
 -------------------------------------------------
|                    |
|                    |                      　　ゴ
|                    |                      
|              ~~~~<[0]>~~~~              　　ゴ
|                   |||     　　　　　　　
|                   +++  　　　　　　　　*MEANACING
|                  -----               
|                 |@@@@@|             　　
|               |[{~***~}]|　
|                 |@@@@@|              
|                  -----             
|                   +++             
|           
|          
|          
|             
|         
|      
|       
|  
|
|
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 _________________________________________________
 """
 ,
 """
 -------------------------------------------------
|                    |
|                    |                      　　ゴ
|                    |                      
|              ~~~~<[0]>~~~~              　　ゴ
|                   |||     　　　　　　　
|                   +++  　　　　　　　　*MEANACING
|                  -----               
|                 |@@@@@|             　　ゴ
|            ---|[{~***~}]|        　　
|                 |@@@@@|              
|                  -----             
|                   +++             
|       
|          
|          
|               
|             
|        
|           
|        
|
|
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 _________________________________________________
 """
 ,
 """
 -------------------------------------------------
|                    |
|                    |                      　　ゴ
|                    |                      
|              ~~~~<[0]>~~~~              　　ゴ
|                   |||     　　　　　　　
|                   +++  　　　         *MEANACING
|                  -----               
|                 |@@@@@|               　ゴ
|            ---|[{~***~}]|---　
|                 |@@@@@|           
|                  -----             
|                   +++             
|       
|          
|          
|               
|             
|        
|           
|        
|
|
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 _________________________________________________
 """
 ,
 """
 -------------------------------------------------
|                    |
|                    |                      　　ゴ
|                    |                      
|              ~~~~<[0]>~~~~              　　ゴ
|                   |||     　　　　　　　
|                   +++  　　　         *MEANACING
|                  -----               
|        ###      |@@@@@|               　ゴ
|       #####---|[{~***~}]|---　
|        ###      |@@@@@|              ゴ
|                  -----             
|                   +++             
|       
|          
|          
|               
|             
|        
|           
|        
|
|
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 _________________________________________________
 """
 ,
 """
 -------------------------------------------------
|                    |
|                    |                      　　ゴ
|                    |                      
|              ~~~~<[0]>~~~~              　　ゴ
|                   |||     　　　　　　　
|                   +++  　　　         *MEANACING
|                  -----        ^      
|        ###      |@@@@@|      ^^^      　ゴ
|       #####---|[{~***~}]|---#####　
|        ###      |@@@@@|      ###     ゴ
|                  -----             
|                   +++             
|       
|          
|          
|               
|             
|        
|           
|        
|
|
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 _________________________________________________
 """
 ,
 """
 -------------------------------------------------
|                    |
|                    |                      　　ゴ
|                    |                      
|              ~~~~<[0]>~~~~              　　ゴ
|                   |||     　　　　　　　
|                   +++  　　　         *MEANACING
|                  -----        ^      
|        ###      |@@@@@|      ^^^      　ゴ
|       #####---|[{~***~}]|---#####　
|        ###      |@@@@@|      ###     ゴ
|                  -----             
|                   +++             ゴ
|                   |||               
|                     
|                
|                          
|                  
|                      
|                    
|               
|
|
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 _________________________________________________
 """
 ,
 """
 -------------------------------------------------
|                    |
|                    |                      　　ゴ
|                    |                      
|              ~~~~<[0]>~~~~              　　ゴ
|                   |||     　　　　　　　
|                   +++  　　　         *MEANACING
|                  -----        ^      
|        ###      |@@@@@|      ^^^      　ゴ
|       #####---|[{~***~}]|---#####　
|        ###      |@@@@@|      ###     ゴ
|                  -----             
|                   +++             ゴ
|                   |||               
|               ||||||     
|               |||    
|               |||         
|               |||     
|                     
|                
|              
|
|
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 _________________________________________________
 """
 ,
 """
 -------------------------------------------------
|                    |
|                    |                      　　ゴ
|                    |                      
|              ~~~~<[0]>~~~~              　　ゴ
|                   |||     　　　　　　　
|                   +++  　　　　　　　　*MEANACING
|                  -----               
|                 |@@@@@|             　　ゴ
|         ###---|[{~***~}]|---###　　
|                 |@@@@@|              ゴ
|                  -----             
|                   +++             ゴ
|                   |||               
|               |||||||||||      
|               |||     |||
|               |||     |||         
|               |||     |||
|                     
|                
|              
|
|
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 _________________________________________________
 """
 ,
  """
 -------------------------------------------------
|                    |
|                    |                      　　ゴ
|                    |                      
|              ~~~~<[0]>~~~~              　　ゴ
|                   |||     　　　　　　　
|                   +++  　　　　　　　　*MEANACING
|                  -----               
|                 |@@@@@|             　　ゴ
|         ###---|[{~***~}]|---###　　
|                 |@@@@@|              ゴ
|                  -----             
|                   +++             ゴ
|                   |||               
|               |||||||||||      ゴ
|               |||     |||
|               |||     |||         
|               |||     |||
|              #####   #####        終了
|              #####   #####     GAME OVER
|              TTTTT   TTTTT
|
|
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 _________________________________________________
 """
    ,
"""
-----------------------------------*
|~~~~      ______                  |
|~~~~     /|_||_\`.__              | 
|~~~~    (   _    _ _\             |
|~~~~    =`-(_)--(_)-'             |
-----------------------------------*
"""
    ,
"""
     .oOOOOOOo.
   oO'        'Oo
  O'  O      O  'O
 O                O
 O                O
 O  Oo,      ,oO  O
  O. 'OOOOOOOO' .O
   Yb.        .dP
     'YOOOOOOP'
"""

)   #Car from https://www.asciiart.eu/vehicles/cars

    #smiley face from https://www.asciiart.eu/computers/smileys

    #define general functions
    man = 0 #determines what parts of the hangman will be displayed
    guesses = 10 #total number of guesses
    diffName = "" #name of difficulty
    finalAnswer = [] #used to check if the input == the word
    display = [] #what is going to be displayed
    warning = 4 #the number of warnings given
    while True:
      diff = input("Select difficulty (input \"E\", \"M\", or \"H\" for Easy, Medium or Hard difficulty): ")
      if diff.upper() == "E":
        diffMod = 1 #for hangman (1 * 10 == 10)
        diffLevel = 10 #to determine output
        diffName = "Easy" #difficulty name
        break
        
      elif diff.upper() == "M":
        diffMod = 2 #for hangman (2 * 5 == 10)
        guesses -= 5 #total of 5 guesses for medium difficulty
        diffLevel = 20 #to determine output
        diffName = "Medium" #difficulty name
        break
        
      elif diff.upper() == "H":
        diffMod = 5 #for hangman (5 * 2 == 10)
        guesses -= 8 #total of 2 guesses for medium difficulty
        diffLevel = 30 #to determine output
        diffName = "Hard" #difficulty name
        break
        
      #for invalid inputs
      else:
        print("Not a difficulty")
        print("\n")



    #Topic 1 = Foods. Topic 2 = FRC stuff. Topic 3 = Celebs. Topic 4 = Animals. Topic 5 = Brands. Topic 6 = Countries.
    print("\n")
    topicList = ["Foods (yo tengo hambre)","FRC stuff (up to 2020 season, most of it is general though)","Famous people (2 seiyuus included in the list because I\'m a weeb)","Animals (Thank you based wikipedia)", "Brands (silence, BRAND)"]


    foods = ['Macaroni, spahgetti, and pasta', 'Sushi, ramen, and soba', 'Hamburgers, hot dogs, and buffalo wings', 'Ice cream, crepes, and parfaits', 'Burritos, tacos, and tamales']
    foodClues = ["Two types of pasta and itself", "Popular Japanese foods","Popular American foods (does not have to originate from America though)","Popular desserts", "Popular Mexican foods"]

    frc_stuff = ['For inspiration and recognition of science and technology', 'Infinite recharge', 'National instruments', 'Dean Kamen', 'FIRST robotics competition']
    frcClues = ["FIRST", "Game this year (2020)", "A important sponsor", "Founder of FIRST", "FRC"]

    #I don't know shit about celebrities, my apologies
    celebs = ['Joaquin Phoenix', 'Kaji Yuki', 'Michael Jackson', 'Masako Nozawa', 'J.S Bach']
    celebClues = ["Played the Joker. (Which one though?)", "Voiced Eren (AoT)", "Annie are you ok?", "Voiced Goku (DBZ)", "Popular Classical musician of the Baroque period"]

    animals = ['Lion-Tailed Macaque', 'Golden retriever, Labrador Retriever, and Flat-Coated Retriever', 'Panda bear, polar bear, and black bear', 'Wunderpus Photogenicus', 'Hammerhead shark, goblin shark, and bull shark']
    animalClues = ["Endangered Old-world monkey", "Types of retriever dogs", "Types of bears", "Octopus with a weird name", "Types of sharks"]

    brands = ['Mcdonalds, In-n-out, and Burger King', 'Nintendo, Microsoft, and Sony', 'Toyota, Honda, and Ford', 'Helwett-Packard', 'Google, Bing, and Yahoo']
    brandClues = ["Burger chains", "The big 3 in video games", "Car brands", "HP", "Search engines. One is part of Microsoft but whatevs"]



    #store lists of topics and clues in a dictionary
    topics = {0: foods, 1: frc_stuff, 2: celebs, 3: animals, 4: brands}
    onTopic = {0: foodClues, 1:frcClues, 2: celebClues, 3: animalClues, 4: brandClues}

    topicIndx = randint(0,4) #picks topic from the topic list
    print("\n")
    print(HANGMAN[man]) #hangman is printed FIRST so all other data can be read
    print("\n")
    print("The topic is: %s." % (topicList[topicIndx]))
    print("\n")
    print("There may be a list of words related the topic, so be careful. The words in the list are related to each other though!")

    theTopic = topics[topicIndx] #topic containing words


    #determine what word is going to be used as the answer
    wordIndx = randint(0,4) 
    #a word that is counted as one element
    unsplitWord = theTopic[wordIndx]
    betaWord = []
    word = []
    guessedLetters = []
    symbols = ["!","@","#","\"","\'","%","-","_",".",",",";",":","<",">","{","}","[","]","|","+","=","*","/","`","~","\\","1","2","3","4","5","6","7","8","9","0"]

    #turn each character in the word into seperate elements
    for i in unsplitWord:
        betaWord += i

    #make a lowercase version of it for checking letters
    for i in betaWord:
        word += i.lower()

    #make a display by replacing all letters with underscores. Spaces and symbols are kept the same.
    for i in range(len(word)):
      if word[i] in symbols:
        display.append(word[i])
        continue
      elif word[i] == " ":
        display.append(" ")
        continue
      display.append("_")

    topicClue = onTopic[topicIndx] #find which topic the clue is on
    wordClue = topicClue[wordIndx] #find the clue itself
    
    #make the word just characters
    for i in word:
      if i not in symbols and i != " ":
        finalAnswer.append(i)
    
    #make a readable answer to display once the game is over
    preAnswer = []
    for i in betaWord:
      if i == " ":
        preAnswer += "   "
        continue
      preAnswer.append(i + " ")
    answer = "".join(preAnswer)


    #keep offering guesses as long as the number of remaining guesses is over 0
    #GENERAL NOTE: Adding 1 to the variable, diffLevel means the game is won. Otherwise, the game is lost.
    while guesses > 0:
        secretKey = []
        preDisplay = []
        
        #make a more readable display by adding extra spaces and converting it into a string.
        for i in display:
          if i == " ":
            preDisplay += "   "
            continue
          preDisplay.append(i + " ")
        fullDisplay = "".join(preDisplay)
        
        #if the number of guesses is 3, offer a hint/clue
        if guesses == 3:
          print("\n")
          print(HANGMAN[man])
          print("\n")
          print("Clue: %s." % (wordClue))


        #if the amount of warnings remaining reaches 0, end the game on a loss
        if warning <= 0: 
          man = 10
          break

        
        print("\n")
        print("Progress: %s. Guesses remaining: %s. Guessed letters: %s." % (fullDisplay,guesses,guessedLetters)) #show progress
        print("\n")
        #the letter is entered here
        letter = input("Enter a letter, or enter the whole word if you know it: ") 


        #make a lowercase version of the input without spaces or symbols
        for i in letter:
          if i not in symbols and i != " ":
            secretKey.append(i.lower())
        
        #display a win message if the word is guessed correctly
        if secretKey == finalAnswer:
          print("\n")
          print(HANGMAN[11])
          print("\n")
          print("You got the secret ending and won!!! The word was: %s. You won on %s difficulty" % (answer, diffName))
          print("\n")
          return diffLevel + 1

        #otherwise, if the input was too long, if there was no input at all/a space as an input, or if the input was a symbol, give a warning
        elif len(letter) > 1 or len(letter) == 0 or letter in symbols or letter == " ":
            print("\n")
            print(HANGMAN[man])
            print("\n")
            print("Invalid input, no penalty this time, warning given. No remaining warnings = INSTANT LOSS! Warnings remaning: %s. " % (warning))
            warning -= 1
            

        #if the letter was already guessed, ask for an input again
        elif letter.lower() in guessedLetters:
          print("\n")
          print(HANGMAN[man])
          print("\n")
          print("You already guessed %s!" % (letter))
          continue

        #if the letter inputted was in the word, replace a underscore with the letter at the same position
        elif letter.lower() in finalAnswer:
            for i in range(len(word)):
                if letter.lower() == word[i]:
                    display[i] = betaWord[i]
            guessedLetters.append(letter.lower())
            print("\n")
            print(HANGMAN[man])
            print("\n")
            print("%s is in this word!" % (letter))
            

            #if all of the underscores are replaced, display a win message
            if display == betaWord:
                print("\n")
                print(HANGMAN[12])
                print("\n")
                print("You win!!! The word was: %s. You won on %s difficulty" % (answer, diffName))
                print("\n")
                return diffLevel + 1

        #if the letter is not in the word, decrement a guess        
        elif letter not in word:
            print("\n")
            print(HANGMAN[man])
            print("\n")
            print("%s is NOT in this word." % (letter))
            guesses -= 1
            man += diffMod
            guessedLetters.append(letter.lower())

    #game over message
    print("\n")
    print(HANGMAN[man])
    print("\n")
    print("You lose, the word was: %s" % (answer))
    print("\n")
    return diffLevel
    











playing = True #determines if the player is still playing
score = 0 #keeps track of the score
winLoss = [] #keeps track of wins, losses, and difficulty of game #x
gameNum = 0 #keeps track of game number
print("A game by: I Had Too Much Free Time Productions")
while playing:
  #increment 1 for each game played
  gameNum += 1

  print("\n")
  print("Current Score: %s" % (score))
  print("\n")
  print("Scoreboard: %s" % (winLoss))
  print("\n")

#keep track of the games
#Check line 469 for difficulty and win/loss determening details
  result = hangman()
  #10 means loss on easy
  if result == 10: 
    winLoss.append("Game number %s: Loss on easy difficulty" % (gameNum))

  #11 means win on easy 
  elif result == 11: 
    winLoss.append("Game number %s: Win on easy difficulty" % (gameNum))
    score += 5

  #20 means loss on medium 
  elif result == 20: 
    winLoss.append("Game number %s: Loss on medium difficulty" % (gameNum))

  #21 means win on medium
  elif result == 21: 
    winLoss.append("Game number %s: Win on medium difficulty" % (gameNum))
    score += 15

  #30 means loss on hard
  elif result == 30: 
      winLoss.append("Game number %s: Loss on hard difficulty" % (gameNum))

  #31 means win on hard    
  elif result == 31: 
      winLoss.append("Game number %s: Win on hard difficulty" % (gameNum))
      score += 30

  #check if the player still wants to play
  while True:
    print("\n")
    gameEnd = input("Replay? (Input \"Y\" or \"N\"): ")
    if gameEnd.upper() == "Y":
      print("\n")
      break
    elif gameEnd.upper() == "N":
      print("\n")
      print("Thank you for playing!")
      playing = False
      break
    else:
      print("\n")
      print("Invalid input")