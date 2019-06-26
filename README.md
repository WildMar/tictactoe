# WELCOME TO TIC-TAC-TOE!
This is a Tic-Tac-Toe Single Page Application (SPA), which you can run and play the classic game of tic-tac-toe against a computer in your very own browser.

Tic-tac-toe is a game in which you are given a board consisting of a 3X3 grid and you and one other player take turns selecting a position on the grid (Player 1 would place an "O", Player 2 would place an "X"). Whoever gets 3 in a row (diagonally, vertically or horizontally) wins!

## Build - Backend
__Disclaimer:__ This project is built with Python 3.7 and is not reverse compatible with Python 2.7 due to loss of support coming [soon](https://pythonclock.org/).


This project uses poetry for package management. Follow the instructions listed [here](https://github.com/sdispater/poetry) to install/use poetry.

A requirements.txt file is also provided for your convenience.

Before doing anything, it is recommended to change directories into the api folder:
```
cd tictactoe/api
```
### Install dependencies

With poetry:

``` 
poetry install
```

Without poetry:
```
pip install -r requirements.txt
```
(Flesh out the build instructions when close to completion)

## Build - Frontend
__Disclaimer:__ This project is built with the most recent version of Node (10.16.0), and Angular CLI (8.0.4)

Before doing anything, it is recommended to change directories into the ui folder:
```
cd tictactoe/ui
```

### Install dependencies

```
npm install
```