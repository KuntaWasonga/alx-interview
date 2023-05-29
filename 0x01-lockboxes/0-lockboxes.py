#!/usr/bin/python3
''' Module for lockboxes task.
'''


def canUnlockAll(boxes):
    '''Function that checks if all boxes
    in list of boxes can be unlocked
    given the first box is unlocked.
    '''
    l = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        box = unseen_boxes.pop()
        if not box or box >= l or box < 0:
            continue
        if box not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[box])
            seen_boxes.add(box)
    return l == len(seen_boxes)