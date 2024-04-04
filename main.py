sizes = {}
f_1 = open('1.txt', 'r', encoding = 'utf-8')
f_2 = open('2.txt', 'r', encoding = 'utf-8') 
f_3 = open('3.txt', 'r', encoding = 'utf-8') 
f_itog  = open('itog.txt', 'a', encoding = 'utf-8')
lines_1 = f_1.readlines()
lines_2 = f_2.readlines()
lines_3 = f_3.readlines()
for_size = [lines_1 , lines_2, lines_3]
if len(lines_1) < len(lines_2) and len(lines_1) < len(lines_3):
    f_itog.write(f'1.txt\n{len(lines_1)}\n{"".join(lines_1)}\n')
    for_size.remove(lines_1)
elif len(lines_2) < len(lines_1) and len(lines_2) < len(lines_3):
    f_itog.write(f'2.txt\n{len(lines_2)}\n{"".join(lines_2)}\n')
    for_size.remove(lines_2)
else:
    f_itog.write(f'3.txt\n{len(lines_3)}\n{"".join(lines_3)}\n')
    for_size.remove(lines_3)

if len(for_size[0]) < len(for_size[1]):
    if for_size[0] == lines_1:
        f_itog.write(f'1.txt\n{len(lines_1)}\n{"".join(lines_1)}\n')
    elif for_size[0] == lines_2:
        f_itog.write(f'2.txt\n{len(lines_2)}\n{"".join(lines_2)}\n')
    else:
        f_itog.write(f'3.txt\n{len(lines_3)}\n{"".join(lines_3)}\n')
    if for_size[1] == lines_1:
        f_itog.write(f'1.txt\n{len(lines_1)}\n{"".join(lines_1)}\n')
    elif for_size[1] == lines_2:
        f_itog.write(f'2.txt\n{len(lines_2)}\n{"".join(lines_2)}\n')
    else:
        f_itog.write(f'3.txt\n{len(lines_3)}\n{"".join(lines_3)}\n')
else:
    if for_size[1] == lines_1:
        f_itog.write(f'1.txt\n{len(lines_1)}\n{"".join(lines_1)}\n')
    elif for_size[1] == lines_2:
        f_itog.write(f'2.txt\n{len(lines_2)}\n{"".join(lines_2)}\n')
    else:
        f_itog.write(f'3.txt\n{len(lines_3)}\n{"".join(lines_3)}\n')
    if for_size[0] == lines_1:
        f_itog.write(f'1.txt\n{len(lines_1)}\n{"".join(lines_1)}\n')
    elif for_size[0] == lines_2:
        f_itog.write(f'2.txt\n{len(lines_2)}\n{"".join(lines_2)}\n')
    else:
        f_itog.write(f'3.txt\n{len(lines_3)}\n{"".join(lines_3)}\n')

f_1.close()
f_2.close()
f_3.close()
f_itog.close()

