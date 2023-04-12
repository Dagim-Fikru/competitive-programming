class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        isWhite = False
        for i in range(1):
            if coordinates[i]=='a' or coordinates[i]=='c' or coordinates[i]=='e' or coordinates[i]=='g':
                if int(coordinates[i+1])%2==0:
                    isWhite= True
            elif coordinates[i]=='b' or coordinates[i]=='d' or coordinates[i]=='f' or coordinates[i]=='h':
                if int(coordinates[i+1])%2!=0:
                    isWhite= True
        return isWhite
                    
                    
                
        