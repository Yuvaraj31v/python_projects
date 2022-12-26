is_continue = True
while (is_continue):

    try:
        value = int(input("Enter a number"))
    except:
        print('Linux function was not executed')
    else:
        print("RUN successful")
        is_continue = False
    finally:
        print("terminated")


