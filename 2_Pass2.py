MNT = [{'index': 0, 'macro_name': 'INCR', 'mdt_index': 0}]
MDT = [(0, 'LDA &A'), (1, 'ADD &B'), (2, 'STA &A'), (3, 'MEND')]
Intermediate_Code = ['START 100', 'INCR 5, 10', 'INCR 6, 12', 'END']
def pass2():
    expanded_code = []
    for line in Intermediate_Code:
        words = line.split()
        if words[0] == 'INCR':  # Check if it's a macro call
            args = words[1].split(',')
            mdt_index = MNT[0]['mdt_index']
            while MDT[mdt_index][1] != 'MEND':
                stmt = MDT[mdt_index][1]
                for i, arg in enumerate(args):
                    stmt = stmt.replace(f'&{chr(65+i)}', arg)  # Replace &A, &B with arguments
                expanded_code.append(stmt)
                mdt_index += 1
        else:
            expanded_code.append(line)
    print("\n".join(expanded_code))
pass2()