import numpy as np
import cv2

class CellCounting:
    def __init__(self):
        pass

    def blob_coloring(self, image):
        """Uses the blob coloring algorithm based on 5 pixel cross window assigns region names
        takes a input:
        image: binary image
        return: a list of regions"""
        
        regions = dict()
        k = 1
        x = y = 0
        area = 0
        height, width = image.shape
        # height = len(image)
        # width = len(image[0])

        visit = np.zeros((height, width), dtype=int)

        def bfs(r, c):
            if not (0 <= r < height and 0 <= c < width):
                return
            if visit[r][c] == 1 or not image[r][c]:
                return

            nonlocal x
            nonlocal y
            nonlocal area
            visit[r][c] = 1
            x += r
            y += c
            area += 1
            
            bfs(r+1, c)
            bfs(r-1, c)
            bfs(r, c+1)
            bfs(r, c-1)

            return
            
        for row in range(height):
            for col in range(width):
                if not visit[row][col] and image[row][col]:
                    bfs(row, col)
                    # print(f"{k}, {int(x/area), int(y/area), area}")
                    regions[k] = ((int(x/area), int(y/area)), area)
                    x = y = area = 0
                    k += 1

        return regions

    def compute_statistics(self, region):
        """Compute cell statistics area and location
        takes as input
        region: list regions and corresponding pixels
        returns: stats"""

        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>
        # print(stats)

        for key, value in region.items():
            print(f"(Region: {key}>, Area: {value[1]}, Centroid: {(value[0][0], value[0][1])}")
            
        return region

    def mark_image_regions(self, image, stats):
        """Creates a new image with computed stats
        Make a copy of the image on which you can write text. 
        takes as input
        image: Input binary image
        stats: stats regarding location and area
        returns: image marked with center and area"""
        new_image = image.copy()

        for key, value in stats.items():
            org = (value[0][1], value[0][0])
            message = '*' + str(key) + ', ' + str(value[1])
            new_image = cv2.putText(new_image, message, org, cv2.FONT_HERSHEY_SIMPLEX, 0.25, (0, 0, 255), 1, cv2.LINE_AA)

        return new_image

