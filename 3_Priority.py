def priority_scheduling():
    n = int(input("Enter the number of processes: "))
    arrival_time = list(map(int, input("Enter arrival times: ").split()))
    burst_time = list(map(int, input("Enter burst times: ").split()))
    priority = list(map(int, input("Enter priorities (lower value means higher priority): ").split()))

    processes = list(zip(arrival_time, burst_time, priority, range(1, n+1)))
    
    processes.sort()

    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    total_waiting_time = 0
    total_turnaround_time = 0

    current_time = 0
    completed = 0
    execution_order = []

    while completed < n:
        idx = -1
        min_priority = float('inf')
        for i in range(n):
            if processes[i][0] <= current_time and processes[i] not in execution_order:
                if processes[i][2] < min_priority:
                    min_priority = processes[i][2]
                    idx = i

        if idx == -1:
            current_time += 1
            continue

        execution_order.append(processes[idx])
        completion_time[idx] = current_time + processes[idx][1]
        turnaround_time[idx] = completion_time[idx] - processes[idx][0]
        waiting_time[idx] = turnaround_time[idx] - processes[idx][1]

        total_waiting_time += waiting_time[idx]
        total_turnaround_time += turnaround_time[idx]

        current_time += processes[idx][1]
        completed += 1

    print("\nProcess\tArrival Time\tBurst Time\tPriority\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"P{processes[i][3]}\t{arrival_time[i]}\t\t{burst_time[i]}\t\t{priority[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print(f"\nAverage waiting time = {total_waiting_time / n:.2f}")
    print(f"Average turnaround time = {total_turnaround_time / n:.2f}")

    print("\nGantt Chart:")
    time = 0
    for process in execution_order:
        print(f"|  P{process[3]}  ", end="")
    print("|")

    time = 0
    for process in execution_order:
        print(f"{time:<7}", end="")
        time += process[1]
    print(f"{time}")

priority_scheduling()
