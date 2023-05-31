def printJobScheduling(arr, t):
    n = len(arr)

    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    result = [False] * t
    job = ['-1'] * t

    for i in range(len(arr)):
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                break

    print("Following is the maximum profit sequence of jobs:")
    print(job)


if __name__ == '__main__':
    arr = []

    num_jobs = int(input("Enter the number of jobs: "))

    for _ in range(num_jobs):
        job_name = input("Enter the job name: ")
        deadline = int(input("Enter the job deadline: "))
        profit = int(input("Enter the job profit: "))

        arr.append([job_name, deadline, profit])

    num_slots = int(input("Enter the number of time slots available: "))

    printJobScheduling(arr, num_slots)
