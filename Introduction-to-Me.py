def myintroduction():
    name = input ("What's your name?")
    right = input ("Are you sure about your answer?Yes or No?")
    if right == "yes":
        print ("Nice to meet you " + name + "!")
        
    else:
        name = input ("What's your name?")
        right = input ("Are you sure about your answer?Yes or No?")
        
    if right == "Yes":
        print ("Nice to meet you " + name + "!")
        age = input ("How old are you " + name + "?")
        right1 = input ("Are you sure about your answer?Yes or No?")
        if right1 == "yes":
            print "You are " + age + " years old."
    else:
        age = input ("How old are you " + name + "?")
    right1 = input ("Are you sure about your answer?Yes or No?")
    
    if right == "yes":
        print "You are " + str(age) + " years old."
        print "This is all the information so far..."
        print "Your name is " + str(name) + "." + "You are " + str(age) + " years old."
        print "Thanks for introducing yourself!"
        print "Your personal information will not be saved or stored in any way for any purpose."
     
        
        
