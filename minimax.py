from player import Player
import copy
import time








class MyPlayer(Player):
    max_duration=0


    def __init__(self, name, dep):
        self.dep=dep
        print(name)
        super().__init__(name)


    def choose_next_move(self, board, letter) -> (int, int):
        start=time.time()
        best_move=(-1,-1)
        best_score= -1000000000
        possible_moves = board.get_possible_moves(letter)


        for move in possible_moves:
            new_board=copy.deepcopy(board) #copy board to simulate a play
            new_board.apply_move(move, letter) #apply the move
            score=self.minimax(new_board, letter,self.dep) #get the best move for a depth of 2


            if score>=best_score: #choosing move and score if the score is the highest we get the best move
                best_score=score
                best_move=move
        end=time.time()
        #print("max is : ",duration)
        duration=end-start
        print("The decision took : ",end-start," seconds")
        if duration > MyPlayer.max_duration:
            MyPlayer.max_duration = duration


        print("max is : ", MyPlayer.max_duration)
        return best_move


    def minimax(self, board, letter, depth):
        if depth==0: #Stop condition
            return len(board.get_indexes_of("B"))-len(board.get_indexes_of("W"))
            
        if letter=="B": #Case of playing team B
            best_score= -1000000000


            for move in board.get_possible_moves(letter):
                new_board=copy.deepcopy(board)
                new_board.apply_move(move, letter)
                score=self.minimax(new_board,"W",depth - 1)
                best_score=max(best_score, score)


            return best_score


        else: #Case of playing team W
            best_score = 1000000000


            for move in board.get_possible_moves(letter):
                new_board=copy.deepcopy(board)
                new_board.apply_move(move, letter)
                score=self.minimax(new_board,"B",depth - 1)
                best_score=min(best_score, score)


            return best_score
