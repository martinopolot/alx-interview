def canUnlockAll(boxes):
    num_of_boxes = len(boxes)
    unlocked = [False] * num_of_boxes
    unlocked[0] = True
    stack = [0]

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key < num_of_boxes and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)

    return all(unlocked)
