class BinaryImage:
    def __init__(self):
        pass

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram as a list"""
        
        hist = [0]*256
        
        for row in range(len(image)):
            for col in range(len(image[row])):
                hist[image[row][col]] += 1

        return hist

    def find_otsu_threshold(self, hist):
        """analyses a histogram to find the otsu's threshold assuming that the input histogram is bimodal.
        takes as input
        hist: a histogram
        returns: an optimal threshold value (otsu's threshold)"""

        varience = float('inf')
        threshold = 0
        image_sum = 65024
        
        for threshold_value in range(256):
            weight_b = sum_b = varience_b = 0
            weight_f = sum_f = varience_f = 0
            mean_b = mean_f = 0

            for val_b in range(0, threshold_value):
                sum_b += hist[val_b]
                mean_b += val_b*hist[val_b]
            for val_f in range(threshold_value, 256):
                sum_f += hist[val_f]
                mean_f += val_f*hist[val_f]

            if not sum_b or not sum_f:
                continue

            weight_b = sum_b / image_sum
            mean_b /= sum_b
            weight_f = sum_f/image_sum
            mean_f /= sum_f
        
            for val_b in range(0, threshold_value):
                varience_b += ((val_b - mean_b)**2)*hist[val_b]
            for val_f in range(threshold_value, 256):
                varience_f += ((val_f - mean_f)**2)*hist[val_f]

            varience_b /= sum_b
            varience_f /= sum_f
            
            in_class_varience = weight_b*varience_b + weight_f*varience_f
            
            if in_class_varience < varience:
                varience = in_class_varience
                threshold = threshold_value
            
        return threshold

    def binarize(self, image):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        Make calls to the compute_histogram and find_otsu_threshold methods as needed.
        take as input
        image: an grey scale image
        returns: a binary image"""

        bin_img = image.copy()

        histogram = self.compute_histogram(image)
        threshold = self.find_otsu_threshold(histogram)
        
        for row in range(len(bin_img)):
            for col in range(len(bin_img[row])):
                bin_img[row][col] = 255 if bin_img[row][col] < threshold else 0
                
        return bin_img




