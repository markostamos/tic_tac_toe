from copy import deepcopy
class Game:
    def __init__(self,player):
        self.board = [['-' for x in range(3)] for y in range(3)]
        self.player = player
        self.old = []
    def restart(self):
        self.board = [['-' for x in range(3)] for y in range(3)]
        self.old = []
        
    def check_winner(self):
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
                    return None
        result["winner"]="DRAW"
        return result

    def move(self,x,y):
        self.old = deepcopy(self.board) 
        if self.isvalid(x,y):
            self.board[x][y] = self.player
            self.nextplayer()
            return True
        
        return False
    
    def undo(self):
        self.board = deepcopy(self.old) 
    def isvalid(self,x,y):
        if x>2 or y>2:return False
        if self.board[x][y]!="-":
            return False
        else:
            return True    
    def AIplay(self):
        return 0,0
        '''
        moves = self.validMoves()
        bestscore = -1
        for board in moves:
            score = self.minimax(True)
            if score>bestscore:
                bestscore=score
                bestboard=board
        self.board = deepcopy(bestboard)
        '''
     

    #TSEK    
    def evaluate(self,board):
        winner = self.check_winner(board)
        if winner =="X":return 1
        if winner =="O":return -1
        else:return 0
    #TSEK    
    def validMoves(self):
        moves = []
        for x in range(3):
            for y in range(3):
                if self.board[x][y] =="-":
                    moves.append((x,y))
        return moves

    def minimax(self,maximizingPlayer):
      pass

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
                self.print()
                
                result = self.check_winner()
                if result!=None:return result
                
        if self.player=="X":
            #x,y = self.AIplay()
            #if self.isvalid(x,y)!=True:return None
            moves = self.validMoves()
            x,y = moves[0]
            self.move(x,y)
            self.print()
        
            
            return self.check_winner()
            
            
    def nextplayer(self):
        if self.player=="O":self.player="X"
        else:
            self.player="O"


