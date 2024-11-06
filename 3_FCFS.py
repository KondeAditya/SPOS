def fcfs_scheduling():
    n = int(input("Enter the number of processes: "))
    arrival_time = list(map(int, input("Enter arrival times: ").split()))
    burst_time = list(map(int, input("Enter burst times: ").split()))

    waiting_time = [0] * n
    turnaround_time = [0] * n
    total_waiting_time = 0
    total_turnaround_time = 0

    for i in range(1, n):
        waiting_time[i] = max(0, waiting_time[i - 1] + burst_time[i - 1] - arrival_time[i] + arrival_time[i - 1])
    for i in range(n):
        turnaround_time[i] = waiting_time[i] + burst_time[i]
        total_waiting_time += waiting_time[i]
        total_turnaround_time += turnaround_time[i]

    print("Process\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"P{i+1}\t{arrival_time[i]}\t\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print(f"\nAverage waiting time = {total_waiting_time / n:.2f}")
    print(f"Average turnaround time = {total_turnaround_time / n:.2f}")

    print("\nGantt Chart:")
    time = 0
    for i in range(n):
        print(f"|  P{i+1}  ", end="")
    print("|")
    time = 0
    for i in range(n):
        print(f"{time:<7}", end="")  
        time += burst_time[i]
    print(f"{time}")
fcfs_scheduling()