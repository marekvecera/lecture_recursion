import matplotlib.pyplot as plt
import numpy as np


def floodfill(img: np.array, x: int, y: int):
    size = np.shape(img)
    if size[0] <= x or size[1] <= y:
        return img
    if img[x,y] == 1:
        img[x,y] = 2
        img = floodfill(img, x+1, y)
        img = floodfill(img, x, y+1)
        img = floodfill(img, x-1, y)
        img = floodfill(img, x, y-1)
    return img


def main():
    img = plt.imread("files/img0.png")[:, :, 0]
    # img = plt.imread("files/img1.png")[:, :, 0]
    # img = plt.imread("files/img2.png")[:, :, 0]

    img = floodfill(img, 0, 0)

    plt.imshow(img, cmap="gray")
    plt.show(block=False)
    plt.pause(5)
    plt.clf()


if __name__ == "__main__":
    main()
