MNT = []   
MDT = []   
Intermediate_Code = []   

def pass1(source_code):
    inside_macro = False
    mnt_index = 0  # MNT index
    mdt_index = 0  # MDT index
    for line in source_code:
        words = line.strip().split()
        if words[0] == "MACRO":  # Start of macro
            inside_macro = True
            MNT.append({"index": mnt_index, "macro_name": words[1], "mdt_index": mdt_index})
            mnt_index += 1
        elif words[0] == "MEND":  # End of macro
            inside_macro = False
            MDT.append((mdt_index, "MEND"))
            mdt_index += 1
        elif inside_macro:  # Inside macro definition
            MDT.append((mdt_index, line.strip()))
            mdt_index += 1
        else:  # Non-macro line
            Intermediate_Code.append(line.strip())

source_code = [
    "MACRO INCR &A &B","LDA &A" ,"ADD &B","STA &A","MEND","START 100","INCR 5, 10","INCR 6, 12","END"
]

pass1(source_code)
print("MNT:", MNT)
print("MDT:", MDT)
print("Intermediate Code:", Intermediate_Code)
