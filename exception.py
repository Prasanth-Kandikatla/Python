# Exception handeling
try:
    f = open("Linux.txt")
    # a = bad_variable
except Exception as e:
    print(e)
except Exception as e:
    print(e)
except IndentationError:
    print("Error!")
else:
    print("This 'else' blockexecutes when there is no exception found!")
finally:
    print("This 'finally' block is executed no matter what!")