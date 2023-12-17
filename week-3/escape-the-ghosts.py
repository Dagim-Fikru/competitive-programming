class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        ghost_distance = 0
        player_distance = abs(target[0])+abs(target[1])
        for i in range(len(ghosts)):
            ghost_distance = abs(target[0]-ghosts[i][0])+abs(target[1]-ghosts[i][1])
            if player_distance >= ghost_distance:
                return False
        return True
