class failedException(Exception):
    def __init__(self):
        super()

is_continue = True
while(is_continue):
    try:
        marks = int(input("Enter your marks"))
        print("Your marks are: " + str(marks))
        if marks < 36:
            raise failedException
    except failedException:
        print("Sorry! You are failed!")
    else:
        print("Congratulations! You are passed")
        is_continue = False
