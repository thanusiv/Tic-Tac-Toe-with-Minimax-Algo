# Tic-Tac-Toe using Minimax Algorithm with Alpha-Beta Pruning

## Table of Contents

- [Overview](#Overview)
- [Demo](#Demo)
- [How to Load Project](#how-to-load-project)
- [Features](#Features)
- [Technologies Used](#technologies-used)
- [Acknowledgements](#acknowledgements)

## Overview

This is a project that showcases the Minimax Algorithm. This project allows the user to play tic-tac-toe against an A.I who uses this algorithm to compute the best move that it can play at the current game state. In addition, I used the Alpha-Beta Pruning optimization technique on the vanilla Minimax Algorithm to speed up computation time. Even though the number of game states in tic-tac-toe is small relative to a game like chess, it sped up how long it took for the A.I to compute it's initial move dramatically. You can go to a previous commit where I didn't implement this technique to see the speed difference. I did not use any depth parameter in my algorithm simply because it would not affect the perceived difference the user will face when playing against the A.I. 

Try this out yourself and see how you fare against it!

## Demo

<img src="gifs/1.gif?raw=true"/> <img src="gifs/2.gif?raw=true"/> <img src="gifs/3.gif?raw=true"/>

## How to Load Project

Simply clone the Github repository to a local directory and open and run the `main.py` file using an IDE or from the terminal.

## Features

- Implemented both the Minimax Algorithm and the Alpha-Beta Pruning optimization technique from scratch
- Allows the user to play against the A.I via the console of the IDE or terminal 
- Tic-tac-toe game was also implemented from scratch and can be altered to a larger grid if wanted
- Use of OOP in Python can be used as template for future projects

## Technologies Used

- [Visual Studio Code](https://code.visualstudio.com/) - IDE used to build the project
- [Python 3.8.3](https://www.python.org/downloads/) - Programming language used

## Acknowledgements

- Thanks to [Codecademy](https://www.codecademy.com/catalog/all) for teaching me about the Minimax Algorithm and Alpha-Beta Pruning!
