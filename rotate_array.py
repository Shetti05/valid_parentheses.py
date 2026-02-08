# rotate_array.py

def rotate_array(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]


if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))
    k = int(input("Enter rotation value k: "))
    print("Rotated Array:", rotate_array(arr, k))
