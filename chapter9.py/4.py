
def generatetable(n):
    table = ""
    for i in range(1,11):
     table += f"{n} X {i} = {n*i}\n"
    with open(f"tables/table_{n}","w") as f:
        f.write(table)


# with open("tables/table","w") as f:
for table in range(2,20):
        generatetable(table)
            