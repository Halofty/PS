class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        max_overlap = 0

        # Create a list of coordinates for the 1s in img1 and img2
        ones_img1 = [(i, j) for i in range(n) for j in range(n) if img1[i][j] == 1]
        ones_img2 = [(i, j) for i in range(n) for j in range(n) if img2[i][j] == 1]

        # Use a dictionary to count the number of overlaps for each translation
        translation_count = {}

        for (x1, y1) in ones_img1:
            for (x2, y2) in ones_img2:
                # Calculate the translation vector
                translation = (x2 - x1, y2 - y1)
                if translation not in translation_count:
                    translation_count[translation] = 0
                translation_count[translation] += 1
                max_overlap = max(max_overlap, translation_count[translation])

        return max_overlap