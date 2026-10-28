import os, time, random, argparse

username = os.getlogin()


parser = argparse.ArgumentParser(
    description="plzdont brick my goddamn pc ftlog"
)
parser.add_argument("--facreset", "-f", action="store_true", help="factory resets")
args = parser.parse_args()
if args.facreset:
    loser = True


def delete_files_lol(dir_path, num_dewl):
    try:
        allitems = os.listdir(dir_path)
    except FileNotFoundError:
        print(f"i didnt find it. sorry? try not to use {dir_path}")
        return
    except PermissionError:
        print(f"do you have {dir_path}'s permission? i think not.")

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


def maingame():
    while True:
        coins = 15000
        input("Press enter to start roulette!")
        


def main():
    print("Welcome to Py Roulette 3K!")
    input("press enter to start")
    maingame()


if __name__ == "__main__":
    main()