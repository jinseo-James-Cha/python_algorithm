class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # binary -> 1 or 0
        # n * n -> n = len(image)
        
        # 1.
        # flip image
        # left right change
        
        # 2. invert an image
        # 0 -> 1 and 1 -> 0
        
        
        """
        [
        [1,1,0],
        [1,0,1],
        [0,0,0]
        ]
        
        1.
        0 1 1
        1 0 1
        0 0 0
        
        2. 
        1 0 0
        0 1 0
        1 1 1
        I got the question !
        
        
        my intuitive solution
        pop and invert
        1 1 0
        pop 0
        if 0 -> 1 and 1 -> 0
        append curr image [1]
        
        1 1
        pop 1
        if 1-> 0
        append curr image [1, 0]
        """
        
        n = len(image)
        res = []
        for i in range(n):
            curr_image = []
            while image[i]:
                invert_x = int(not image[i].pop())
                curr_image.append(invert_x)
            res.append(curr_image[:])
        return res
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