print('This program is a basic calculator that allows you to perform calculations using two numbers and a character that indicates which math operation to perform. Options for the characters are + - * / and %.')
 
while True:
    char = input("Enter q to Quit, otherwise operator (+, -, * /): ")
     
    if char.lower() == 'q':
        break
 
    if char not in '+-*/q':
        print('Invalid entry')        
        continue
 
    a = float(input('Enter a number: ')) 
    b = float(input('Enter another number: ')) 
  
    if char == '+': 
        sum = a + b 
        print('The sum of ',a, ' and ', b,' is ', sum , sep = '')
  
    elif char == '-': 
        difference = a-b 
        print(a, ' minus ', b, ' equals ', difference, '.', sep = '')
  
    elif char == '*':  
        product = a*b  
        print(a, ' times ', b, ' equals ', product, '.', sep='')
  
    elif char == '/': 
  
        if b == 0: 
            print('You can not divide a number by zero.')
  
        else: 
            quotient = a/b 
            rounded = format(quotient, '.2f') 
            print(a, ' divided by ', b, ' equals ', rounded, '.', sep = '')
  
    elif char == '%': 
        remainder = a%b 
        print('The remainder of ',a, ' and ', b, ' is ', a%b, '.', sep='') 
  
  
    else:
        print('That is not a valid character. Please enter + - * / or %.')
 
print('Goodbye')
