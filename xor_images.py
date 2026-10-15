import cv2

# Load the two images (must be the exact same size)
img1 = cv2.imread('./flag_7ae18c704272532658c10b5faad06d74.png')
img2 = cv2.imread('./lemur_ed66878c338e662d3473f0d98eedbd0d.png')

# Perform the bitwise XOR operation
xor_result = cv2.bitwise_xor(img1, img2)

# Save and display the result
cv2.imwrite('xor_output.png', xor_result)
cv2.imshow('XOR Result', xor_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
