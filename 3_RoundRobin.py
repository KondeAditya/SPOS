def round_robin():
    n = int(input("Enter the number of processes: "))
    arrival_time = list(map(int, input("Enter arrival times: ").split()))
    burst_time = list(map(int, input("Enter burst times: ").split()))
    quantum = int(input("Enter time quantum: "))

    remaining_burst_time = burst_time[:]
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completion_time = [0] * n
    total_waiting_time = 0
    total_turnaround_time = 0
    current_time = 0
    execution_order = []
    
    queue = []
    for i in range(n):
        queue.append(i)
    
    while queue:
        process = queue.pop(0)
        
        if remaining_burst_time[process] > quantum:
            remaining_burst_time[process] -= quantum
            current_time += quantum
            queue.append(process)  
            execution_order.append(f"P{process+1}")
        else:
            current_time += remaining_burst_time[process]
            completion_time[process] = current_time
            remaining_burst_time[process] = 0
            execution_order.append(f"P{process+1}")

    for i in range(n):
        turnaround_time[i] = completion_time[i] - arrival_time[i]
        waiting_time[i] = turnaround_time[i] - burst_time[i]
        total_waiting_time += waiting_time[i]
        total_turnaround_time += turnaround_time[i]

    print("\nProcess\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"P{i+1}\t{arrival_time[i]}\t\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print(f"\nAverage waiting time = {total_waiting_time / n:.2f}")
    print(f"Average turnaround time = {total_turnaround_time / n:.2f}")

    print("\nGantt Chart:")
    time = 0
    for proc in execution_order:
        print(f"| {proc} ", end="")
    print("|")

    time = 0
    for proc in execution_order:
        print(f"{time:<5}", end="")
        time += quantum
    print(f"{time}")

round_robin()
