# Pyroulette

### An python project for [scraps](https://scraps.hackclub.com).


The whole point of this project is simple, an cassino roulete in cli, that if you get the number wrong, it will delete random files from your system. 
## How it works:
- Execute the application
- Choose a number
- Right number, more coins. Wrong number, Less coins.
- When coins = 0, runs an func that deletes random files from your root folder. (C:\ in Windows, / in Linux)

| Running the executable | What does it do |
|----------|----------|
| ./main-linux  | Runs it on your root folder. If on a vm, use sudo for + destruction   |
| ./main-linux --plzdontbrick   | Only deletes files from the folder you're running it.   | 

### Made by [compiling.me :3](https://compiling.me)
