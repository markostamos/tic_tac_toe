from copy import deepcopy
class Game:
    def __init__(self,player):
        self.board = [['-' for x in range(3)] for y in range(3)]
        self.player = player
        self.old = []
    def restart(self):
        self.board = [['-' for x in range(3)] for y in range(3)]
        self.old = []
        
    def check_winner(self,board = None):
        if board is None:
            board = self.board
        result = dict(type=None,pos=None,winner=None)
        for i in range(3):
            if board[i][0]==board[i][1]==board[i][2]!='-':
                result["winner"]=board[i][0]
                result["type"]="horizontal"
                result["pos"]=i
                return result
        for j in range(3):
            if board[0][j]==board[1][j]==board[2][j]!='-':
                result["winner"]=board[0][j]
                result["type"]="vertical"
                result["pos"]=j
                return result
        if board[0][0]==board[1][1]==board[2][2]!='-':
            result["winner"]=board[0][0]
            result["type"]="desc"
            return result
        elif board[0][2]==board[1][1]==board[2][0]!='-':
            result["winner"]=board[0][2]
            result["type"]="asc"
            return result
        for x in board:
            for y in x:
                if y=="-":
                    return result
        result["winner"]="DRAW"
        return result

    def move(self,x,y):
        if self.isvalid(x,y):
            self.board[x][y] = self.player
            self.nextplayer()
            return True
        
        return False
    
    def undo(self):
        self.board = deepcopy(self.old)
        self.nextplayer()
    def isvalid(self,x,y):
        if x>2 or y>2:return False
        if self.board[x][y]!="-":
            return False
        else:
            return True    
    def AIplay(self):
        moves = self.validMoves()
        bestscore = -100000
        for x in moves:
            board = deepcopy(self.board)
            board[x[0]][x[1]] = "X"
            score = self.minimax(board,maximizingPlayer=False,alpha=-100,beta=100)
            if score>=bestscore:
                bestscore = score
                best_move = x
        return best_move
     

    #TSEK    
    def evaluate(self,board):
        winner = self.check_winner(board)
        if winner =="X":return 1
        if winner =="O":return -1
        else:return 0
    #TSEK    
    def validMoves(self,board=None):
        if board is None:
            board = self.board
        moves = []
        for x in range(3):
            for y in range(3):
                if board[x][y] =="-":
                    moves.append((x,y))
        return moves

    def minimax(self,board,maximizingPlayer,alpha,beta):
        winner = self.check_winner(board)["winner"]
        if winner is not None:
            if winner=="X":
                return 100
            elif winner=="O":
                return -100
            else:
                return 0
        if maximizingPlayer:
            maxEval = -10000
            moves = self.validMoves(board)
            for x in moves:
                board2 = deepcopy(board)
                board2[x[0]][x[1]] = "X"
                eval = self.minimax(board2,False,alpha,beta)
                maxEval = max(maxEval,eval)
                alpha = max(alpha,eval)
                if beta<= alpha:
                    break
            return maxEval
        else:
            minEval = 10000
            moves = self.validMoves(board)
            for x in moves:
                board2 = deepcopy(board)
                board2[x[0]][x[1]] = "O"
                eval = self.minimax(board2,True,alpha,beta)
                minEval = min(minEval,eval)
                beta = min(beta,eval)
                if beta<=alpha:
                    break
            return minEval

    def print(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i][j]," ",end="")
            print("")  
        return self.board
    #revise
    def play(self,x,y):
       
        if self.player=="O":
            if self.isvalid(x,y):
                self.move(x,y)
                
                result = self.check_winner()
                if result["winner"] is not None:return result
            else:
                return None

                
        if self.player=="X":
            x,y = self.AIplay()
           
            self.move(x,y)
           
        
            
            return self.check_winner()
            
            
    def nextplayer(self):
        if self.player=="O":self.player="X"
        else:
            self.player="O"


