import os


r = 3
d = 0
k = 3
ordreImportant = 1

iter = "Iterative"
recurse = "Recursif"

filename = f"TFJM-2021-Pb1-{iter}.py"
inputFile = "in"


for n in range(2,8):
    # with open("in", "w") as f:
    #     f.write(f"{r} {n} {d} {k} {ordreImportant}")
    # print(f" ========= {r} {n} {d} {k} {ordreImportant} =========")
    os.system(f"echo {r} {n} {d} {k} {ordreImportant} | python {filename}")   