print('Collatz Sequence')

def collatz(number):

    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

while True:
    
    try:
        user_input = int(input('Please enter a number: '))
        
        if user_input <= 1:
            print('Try any number bigger than 1')
            
        while user_input > 1:
            user_input = collatz(user_input)
        
    except ValueError:
        print('Your input must be a number!')
        
    break


        
