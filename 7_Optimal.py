def optimal_pg_replacement():
    pgs = list(map(int, input("Enter Page numbers: ").split()))
    fsize = int(input("Enter Frame size: "))
    memory = []
    pg_fault = 0
    print(f"Pages: {pgs}")
    print(f"Frame size: {fsize}")

    for i, pg in enumerate(pgs):
        # Check if the page is already in memory
        if pg not in memory:
            pg_fault += 1
            # If memory is full, apply optimal replacement strategy
            if len(memory) >= fsize:
                # Find the page in memory that won't be used for the longest time
                future_indices = []
                for mem_pg in memory:
                    if mem_pg in pgs[i + 1:]:
                        future_indices.append(pgs[i + 1:].index(mem_pg))
                    else:
                        # Page not used in the future
                        future_indices.append(float('inf'))
                
                # Remove the page with the highest index (not used for the longest time)
                remove_idx = future_indices.index(max(future_indices))
                memory.pop(remove_idx)
            
            # Add the new page to memory
            memory.append(pg)
            print(f"Page Fault for page {pg}: memory = {memory}")
        else:
            print(f"Page {pg} already exists in memory = {memory}")

    print(f"Number of Page Faults: {pg_fault}")

optimal_pg_replacement()