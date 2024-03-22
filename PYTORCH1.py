
from matplotlib import pyplot as plt
from PIL import Image
from torchvision import transforms


transform = transforms.Compose(
    [
        transforms.RandomCrop(size=(512, 512)),
        transforms.Pad(padding=50, fill=(127, 127, 255), padding_mode="constant")
    ]
)

image = Image.open("cat.jpg")
transformed_image = transform(image)
plt.imshow(transformed_image)
