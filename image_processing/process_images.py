from image_processor import ImageProcessor

test_image = ImageProcessor("images/test_image.jpg")

region = test_image.crop()
region.show()