import cv2
from pyzbar import pyzbar

def scan_upc(image_path):
    try:
        # Load the image
        image = cv2.imread(image_path)

        # Rest of your code
        # ...
    except Exception as e:
        print(f"Error loading the image: {e}")

# Rest of your code
# ...

def scan_upc(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use pyzbar to detect barcodes in the grayscale image
    barcodes = pyzbar.decode(gray)

    # Process each detected barcode
    for barcode in barcodes:
        # Extract the barcode data and type
        data = barcode.data.decode("utf-8")
        barcode_type = barcode.type

        # Print the UPC data and type
        print(f"Found {barcode_type} barcode: {data}")

    # Display the image with bounding boxes around detected barcodes
    cv2.imshow("UPC Scanner", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == "__main__":
    # Replace 'path/to/your/image.jpg' with the path to your image file
    image_path = "C:\\Users\\HP\\Desktop\\jarves\\new\\WhatsApp Image 2023-07-15 at .jpg"


    scan_upc(image_path)
