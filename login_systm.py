TEXT = "login info.txt"

white_list = dict()

def get_white_list():
    try:
        with open(TEXT) as raw_info:
            for line in raw_info:
                user_name, pasword = line.split(" ")
                pair = {user_name: pasword[:-1]}
                white_list.update(pair)
    except OSError as problem:
        print("there is a problem:",problem)
        exit(1)
    return white_list

def check_user_name(put_in_name):
    if put_in_name not in white_list:
        print("no matches, try again")
        return False
    else:
        return True

def check_password(put_in_pass, put_in_name):
    if put_in_pass == white_list[put_in_name]:
        return True
    else:
        return False

def main():
    get_white_list()
    counter = 0
    get_white_list()
    put_in_name = input("Please enter username: ")
    if check_user_name(put_in_name):
        while counter < 4:
            put_in_pass = input("Please enter password: ")
            if check_password(put_in_pass, put_in_name):
                print("Welcome Back!")
                exit("choosing us thanks")
            else:
                counter += 1
                print("wrong password, try again")
                if counter == 3: print("last chance tho")
        print("U ARE OUT!")
    else:
        main()

if __name__ == '__main__':

    main()