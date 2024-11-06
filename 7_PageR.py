from collections import deque
def pg_replacement():

    pgs=list(map(int,input("Enter Page numbers: ").split()))
    fsize=int(input("Enter Frame size: "))
    memory=deque()
    pg_fault=0

    print(f"Pages: {pgs}")
    print(f"Frame size: {fsize}")

    for pg in pgs:
        if pg not in memory:
            pg_fault+=1
            if len(memory)>=fsize:
                memory.popleft()
            memory.append(pg)
            print(f"Page Fault for page{pg} memory= {list(memory)}")
        else:
            memory.remove(pg)
            memory.append(pg)
            print(f"Page {pg} already exists memory= {list(memory)}")
    print(f"Number of Page Faults: {pg_fault}")

pg_replacement()