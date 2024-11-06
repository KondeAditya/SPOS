def preemptive_sjf():
    n = int(input("Enter the number of processes: "))
    arrival_time = list(map(int, input("Enter arrival times: ").split()))
    burst_time = list(map(int, input("Enter burst times: ").split()))

    remaining_time = burst_time[:]  # Copy of burst_time to track remaining time
    waiting_time = [0] * n
    turnaround_time = [0] * n
    complete = 0
    time = 0
    min_remaining_time = float('inf')
    shortest = -1
    check = False
    gantt_chart = []  # To store the process execution order

    while complete != n:
        # Find the process with the minimum remaining time at this time
        for i in range(n):
            if (arrival_time[i] <= time and remaining_time[i] < min_remaining_time and remaining_time[i] > 0):
                min_remaining_time = remaining_time[i]
                shortest = i
                check = True

        if not check:  # No process is ready at this time, increase time
            time += 1
            gantt_chart.append("Idle")  # Indicate idle time in the Gantt chart
            continue

        # Process with the shortest remaining time is selected
        remaining_time[shortest] -= 1
        gantt_chart.append(f"P{shortest + 1}")  # Track the current process in the Gantt chart
        min_remaining_time = remaining_time[shortest]

        if min_remaining_time == 0:
            min_remaining_time = float('inf')

        # If a process is completed
        if remaining_time[shortest] == 0:
            complete += 1
            check = False

            finish_time = time + 1
            waiting_time[shortest] = finish_time - burst_time[shortest] - arrival_time[shortest]

            if waiting_time[shortest] < 0:
                waiting_time[shortest] = 0

            turnaround_time[shortest] = burst_time[shortest] + waiting_time[shortest]

        time += 1

    total_waiting_time = sum(waiting_time)
    total_turnaround_time = sum(turnaround_time)

    print("Process\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"P{i+1}\t{arrival_time[i]}\t\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print(f"\nAverage waiting time = {total_waiting_time / n:.2f}")
    print(f"Average turnaround time = {total_turnaround_time / n:.2f}")

    # Display Gantt Chart with proper alignment
    print("\nGantt Chart:")
    for p in gantt_chart:
        print(f"| {p:^4} ", end="")
    print("|")

    # Print timeline under the Gantt chart
    print("0", end="")  # Start time
    time_counter = 1
    for i in range(len(gantt_chart)):
        print(f"{time_counter:>7}", end="")  # Align each time unit with process labels
        time_counter += 1
    print()  # New line after timeline

preemptive_sjf()
