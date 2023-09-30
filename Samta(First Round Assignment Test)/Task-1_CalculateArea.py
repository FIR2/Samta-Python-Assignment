# ---------  Define the calculate_area function:-------- 
def calculate_area(length, width):
  #AREA IS ALWAYS NON-NEGATVE value,length and width are typically considered to be positive values.
  #So I can Handle first 
    if length < 0: 
        length = -length;
    if width  < 0: 
        width = - width
  # check whether the length is equal to the width
    if length == width:
        return "This is a square!"
    else:
        return length * width     #otherwise return the area by multiplying length and width.

# Create the main function:--> main function to handle the user input and calling the calculate_area function.   
def main():
    # Handle try and expect  errors bymistek user enter input a string then i can handle through try , except
    try:
      length = float(input("Enter the length: "))
      width  = float(input("Enter the width: "))
    
      Area = calculate_area(length, width)
    # check type of  Area it is string or numeric 
      if isinstance(Area, str):
          print(Area)
      else:
          print(f"The area of the rectangle is {Area}")

    except ValueError: 
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
