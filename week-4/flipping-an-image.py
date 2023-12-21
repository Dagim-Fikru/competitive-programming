class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            for j in range(len(image)):
                for k in range(j+1,len(image[j])):
                    image[i][j],image[i][k] = image[i][k],image[i][j]
        for i in range(len(image)):
            for j in range(len(image[i])):
                if image[i][j]==1:
                    image[i][j]=0
                else:
                    image[i][j]=1
        return image