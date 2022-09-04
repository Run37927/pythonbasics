def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

    in_first_row = 'red' if redShirtHeights[0] < blueShirtHeights[0] else 'blue'

    for i in range(len(redShirtHeights)):
        if in_first_row == 'red':
            if redShirtHeights[i] >= blueShirtHeights[i]:
                return False
        else:
            if blueShirtHeights[i] >= redShirtHeights[i]:
                return False
    return True

red = [5, 8, 1, 3, 4]
blue = [6, 9, 2, 4, 5]

print(classPhotos(red, blue))