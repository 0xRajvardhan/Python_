for i in range(2, 21):
    with open(f"Chapter 9/tables/Multiplication_table_of_{i}.txt", 'w') as f:
        for j in range(1, 11):
            f.write(f"{i}X{j}={i*j}\n")
            if j != 10:
                f.write('\n')
        # break --if you remove this break here, the program will print 20 different files of tables from 2 to 20
