def display(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


def insertionSort(array):
    # Iterate through each element in the array, starting from the second element (index 1)
    for step in range(1, len(array)):
        key = array[step]  # Current element to be inserted into the sorted subarray
        j = step - 1  # Index of the last element in the sorted subarray
        print("The current key is ",key)
        # Move elements of the sorted subarray that are greater than the key
        # to one position ahead of their current position
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]  # Shift the element to the right
            j = j - 1
            
            display(array)

            # Display the array after each swap for visualization
            # print(f'Swap: {array[j]} <-> {array[j+1]}')
            # print(array)

        # Place the key at the correct position in the sorted subarray
        array[j + 1] = key
        # print(array)

def insertionSortMain(arr):
    print("========== Insertion Sort============\n")
    insertionSort(arr)

    # Display the sorted array
    print('Sorted Array in Ascending Order:')
    print(arr)
    
# Take user input for the array
if __name__ =='__main__':
    data = input('Enter elements separated by spaces: ').split()
    data = [int(x) for x in data]

    insertionSort(data)

    # Display the sorted array
    print('Sorted Array in Ascending Order:')
    print(data)
