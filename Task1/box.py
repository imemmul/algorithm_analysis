import sys

def calculate(boxes):
    boxes.sort(key=lambda box: (box[0], box[1], box[2]))  # sorting boxes by ascending dimensions
    dp_list = [1] * len(boxes)  # init dynamic programming list to 1 each dp index represents maximum number of nesting depths for each box
    for i in range(len(boxes)):
        for j in range(i): # checking every smaller length box if it fits into current box
            if boxes[i][0] > boxes[j][0] and boxes[i][1] > boxes[j][1] and boxes[i][2] > boxes[j][2]: # checking boxes 
                dp_list[i] = max(dp_list[i], dp_list[j] + 1)  # update dp value for current box
    return max(dp_list)  # return maximum nesting depth

if __name__ == "__main__":
    filename = sys.argv[-1]
    try :
        file = open(filename, 'r')
        lines = file.readlines()
        n = int(lines[0]) # number of booxes
        
        boxes = []
        for i in range(1, len(lines)):
            boxes.append(lines[i].split(' '))
            for j in range(3):
                # print(boxes)
                boxes[i-1][j] = float(boxes[i-1][j])
        # print(boxes)
        print(calculate(boxes))
    except:
        print(f"File not found, please check.")