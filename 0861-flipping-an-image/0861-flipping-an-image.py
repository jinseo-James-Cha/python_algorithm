class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # 1. flip horizontally -> 1 1 0 ->  0 1 1
        # 2. invert -> 0 1 1 -> 1 0 0 
        # 3. return

        n = len(image)
        # v2:
        for i in range(n):
            for j in range(( n + 1 ) // 2):
                image[i][j], image[i][~j] = image[i][~j] ^ 1, image[i][j] ^ 1
        return image

        # v1 
        # 1. flip
        # for i in range(n):
        #     for j in range(n // 2):
        #         image[i][j], image[i][n-j-1] = image[i][n-j-1], image[i][j]
        
        # # 2. invert
        # for i in range(n):
        #     for j in range(n):
        #         image[i][j] = (image[i][j] + 1) % 2

        # return image