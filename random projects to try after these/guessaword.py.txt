word = "duck"
guesses = ''

lives = 4
while lives > 0:         

    failed = 0             

      
    for char in word:      

        if char in guesses:    
    
            print char,

        else:
    
            print "_",     
       
            failed += 1    

    if failed == 0:        
        print "You won"  


        break              

    guess = raw_input("guess a character:") 
  
    guesses += guess                    

    if guess not in word:  
 
        lives -= 1        
 
        print "Wrong"
 
        print "You have", + lives, 'more guesses' 
 
        if lives == 0:           
    
            print "You Lose"
          