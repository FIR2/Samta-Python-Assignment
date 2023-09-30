# -------- create a function to generate series ----------- 
def fibonacci_series(n):
    # Initialize the sequence with the first two terms
    fib_sequence = [0, 1]  

 # new term ko add kiya fib_sequence mein, sequence ke length tak
    while len(fib_sequence) < n:
        Nterm = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(Nterm)

    return fib_sequence

def userInput():
    # handle kiya try except errors ko yadi input non-integer hai to
    try:
        n = int(input("Enter the number of Fibonacci terms to generate: "))
   
       #check kara input value positive hai ya nahi , agar nigative hai to user ko prompt karo enter a positive integer
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            fib_sequence = fibonacci_series(n)    # yadin input valid hai to call kiya fibonacci_series ko
            print(f"Fibonacci sequence up to {n} terms: {fib_sequence}")

    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    userInput()






