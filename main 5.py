import random

def treasure_hunt():
    
    length = random.randint(5, 20)  
    width = random.randint(5, 20)   
    
    
    print(f"The grid dimensions are {length} (length) x {width} (width)")
    
   
    s1 = random.randint(1, length)
    s2 = random.randint(1, width)
    
    attempts = 0
    
    # Guess row position
    print("Guess the row position of the treasure:")
    while True:
        row_guess = int(input("Enter your row guess: "))
        attempts += 1
        
        if row_guess < s1:
            print(f"You guessed too low for the row position, try again! {attempts} attempts used.")
        elif row_guess > s1:
            print(f"You guessed too high for the row position, try again! {attempts} attempts used.")
        else:
            print(f"You guessed correctly! {attempts} attempts used, now try to guess the column position!")
            break
    
    # Guess column position
    print("Guess the column position of the treasure:")
    while True:
        col_guess = int(input("Enter your column guess: "))
        attempts += 1
        
        if col_guess < s2:
            print(f"You guessed too low for the column position, try again! {attempts} attempts used.")
        elif col_guess > s2:
            print(f"You guessed too high for the column position, try again! {attempts} attempts used.")
        else:
            print(f"You guessed the position of the treasure correctly! {attempts} attempts used.")
            break


treasure_hunt()
