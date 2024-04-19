import os

if __name__ == '__main__':
    print("welcome to speakers")
    while True:
        x = input("Enter what you want me to pronounce...")
        if x == 'q':
            os.system("echo 'bye bye dost'")
            break
        command = f" echo {x}"
        os.system(command)


