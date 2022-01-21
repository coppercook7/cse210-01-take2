def main():
    player = next_player("")
    board = create_game()
    while not (winner(board) or draw(board)):
        display_board(board)
        make_move(player, board)
        player = next_player(player)
    display_board(board)
    print("Good game. Thanks for playing!") 
