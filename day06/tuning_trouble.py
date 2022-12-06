import os


def isMarker(str):
    for c in str:
        if str.count(c) > 1:
            return False
    return True


def getMarkerPosition(file: str, marker_length):
    current_python_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(current_python_path, file)
    with open(filepath) as f:
        data = f.read()
        for index in range(0, len(data)):
            if isMarker(data[index : index + marker_length]):
                return index + marker_length


if __name__ == "__main__":
    print(getMarkerPosition("data.csv", 14))
