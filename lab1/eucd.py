X = [1, 2, 3, 4, 5]
Y = [2, 3, 4, 5, 6]

distances = []
for i in range(len(X)):
    distance = ((X[i] - Y[i]) ** 2) ** 0.5
    distances.append(distance)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

sorted_distances = bubble_sort(distances)

print("Sorted Distances:", sorted_distances)
