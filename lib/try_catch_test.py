
def is_going_tobe_error():
    raise ValueError("This is a Value Error big boioioioioioioioioioioioioioioio")

def try_catch():
    try:
        is_going_tobe_error()
    except:
        print("oops this was an error")

