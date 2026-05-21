win_state = False
all_win_coords = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (7, 5, 3))
playing_field = list(range(1, 10))
counter = 0
position = 0
while win_state == False:
    valid = True
    for i in range(1, 10, 3):
        print("|", playing_field[i-1], "|", playing_field[i], "|", playing_field[i+1], "|")
    if counter % 2 == 0:
        player = "0"
    else:
        player = "X"
    print("Ход игрока", player)
    counter += 1
    while valid == True:
        position = int(input("Куда хотите поставить " + player + "? "))
        if playing_field[position-1] == "0" or playing_field[position-1] == "X":
            print("Эта клетка уже занята!")
            valid = True
        else:
            playing_field[position-1] = player
            valid = False
    if counter > 4:        
        for first, second, third in all_win_coords:
            if playing_field[first-1] == playing_field[second-1] == playing_field[third-1]:
                win_state = True
                print("Поздравляем, победил игрок " + player + "!")
        if counter > 8 and win_state == False:
            win_state = True
            print("Ничья!")
