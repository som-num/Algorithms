from tabulate import tabulate

def printJobScheduling(arr, t):
    n = len(arr)

    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    result = [False] * t
    job = ['-1'] * t
    total_profit = 0

    for i in range(len(arr)):
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                total_profit += arr[i][2]
                break

    # Organize the results in a table
    job_table = []
    for i in range(t):
        job_table.append([i + 1, job[i]])

    headers = ["Time Slot", "Job"]
    scheduling_table = tabulate(job_table, headers, tablefmt="fancy_grid")

    # Organize the given jobs in a table
    given_jobs_table = tabulate(arr, headers=["Job", "Duration", "Profit"], tablefmt="fancy_grid")

    print("Given Jobs:")
    print(given_jobs_table)
    print("\nFollowing is the maximum profit sequence of jobs:")
    print(scheduling_table)
    print(f"Total Profit: {total_profit}")

if __name__ == '__main__':
    arr = [['a', 2, 100],  # Job Array
           ['b', 1, 19],
           ['c', 2, 27],
           ['d', 1, 25],
           ['e', 3, 15]]

    printJobScheduling(arr, 3)
