'''
mino stoto
4.22.23

I utilized a recursive version of a merge sort function. It's by no stretch an original idea, but I learned a lot by doing so. It's so elegant,
I love it.
The layout is basic pysimplegui stuff. The program takes user-input data, turns it into an array, and then sorts it with the merge-sort function
when the 'sort' button is clicked. It then uses the binary search function to find a queried integer within the sorted data set.

run the program, then follow the on-screen prompts. input comma-separated integers, then click 'sort'. input a search querie, then click 'search'.
the program will display the results under their respective input boxes. click 'quit' to quit.
'''

import PySimpleGUI as sg

#O(n log n)
def merge_sort(arr):
    cycle = 0 #indexes iterations throughout the function

    if len(arr) > 1: #checks to see that there's more than one integer in the array
        mid = len(arr) // 2 #cuts the array in half
        left_half = arr[:mid] #declares the left half array. the colon calls everything left of the midpoint
        right_half = arr[mid:] #declares the right half array. the colon calls everything right of the midpoint

        #recursively sort the left and right halves while also indexing iterations
        cycle += merge_sort(left_half) #this def was not
        cycle += merge_sort(right_half) #an original thought
        #i learned how factorials really work
        #and have a better idea of recursion
        #which is very cool

        #merge the sorted left and right halves
        i = j = k = 0 #i is the index of the right half, j is the index of the left half, k is the index of the merged array. one line!
        
        while i < len(left_half) and j < len(right_half): #checks that there are any integers left to sort thru at any given time
            if left_half[i] < right_half[j]: #compares integers
                arr[k] = left_half[i] #if i is lower than j, it is copied to k
                i += 1 #advances the marker
            else:
                arr[k] = right_half[j] #if j is lower than i, it is copied to k
                j += 1 #advances the marker
            k += 1 #advances the marker
            cycle += 1 #adds to the iteration index

        #copy remaining elements from the left or right halves, which are already sorted by proxy of remainder
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            cycle += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            cycle += 1

    return cycle
#O(log n)
def binary_search(arr, key):
    # First start out looking at the whole array
    start = 0
    end = len(arr) - 1
    found = -1
    cycle = 0 #tracks total iterations in search
    while found < 0 and start <= end:
        # Calculate midway between start and end
        midway = int((start + end) / 2)
        if arr[midway] == key:
            # We found it!
            found = midway
            cycle += 1
        elif arr[midway] < key:
            # Value must be to the right
            start = midway + 1
            cycle += 1
        else:
            # Value must be to the left
            end = midway - 1
            cycle +=1

    return found, cycle


layout = [
    [sg.Text('Enter a list of integers, separated with commas.')],
    [sg.Input(key='-INPUT-')],
    [sg.Button('Sort')],
    [sg.Text('Sorted array:')],
    [sg.Text(key='array')],
    [sg.Text('Iterations required:')],
    [sg.Text(key='cycle')],
    [sg.Text('Search for an integer:')],
    [sg.Input(key='-Search-')],
    [sg.Button('Search')],
    [sg.Text('Querie found at index:')],
    [sg.Text(key='index')],
    [sg.Text('Iterations required:')],
    [sg.Text(key='cycle2')], 
    [sg.Button('Quit')]
]

# Create a single window with our layout
window = sg.Window('Window Title', layout)

def main():
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
        elif event == 'Sort':
            data = values['-INPUT-']
            arr = [int(x) for x in data.split(",")]
            cycle = merge_sort(arr)
            window['array'].update(str(arr))
            window['cycle'].update(str(cycle))
        elif event == 'Search':
            searched = int(values['-Search-'])
            found, cycle2 = binary_search(arr, searched)
            if found == -1:
                found = 'It was not found, actually.'
            window['index'].update(str(found+1))
            window['cycle2'].update(str(cycle2))

    window.close()

if __name__ == '__main__':
    main()