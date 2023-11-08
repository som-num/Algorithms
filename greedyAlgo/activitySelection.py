from tabulate import tabulate

def printMaxActivities(s, f):
    n = len(f)
    activities = []

    for i in range(n):
        activities.append([i + 1, s[i], f[i]])

    print("Activities Table:")
    headers = ["Activity", "Start Time", "Finish Time"]
    table = tabulate(activities, headers, tablefmt="fancy_grid")
    print(table)

    i = 0
    print("\nThe following activities are selected:")
    print(f"{i+1} (Activity {i+1})")

    for j in range(n):
        if s[j] >= f[i]:
            print(f"{j+1} (Activity {j+1})")
            i = j

# Driver program to test above function
s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]

printMaxActivities(s, f)
