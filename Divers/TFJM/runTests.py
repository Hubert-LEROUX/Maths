import os


r = 3
d = 0
k = 2
ordreImportant = 0
filename = "TFJM-2021-Pb1.py"
inputFile = "in"


for n in range(2,12):
    # with open("in", "w") as f:
    #     f.write(f"{r} {n} {d} {k} {ordreImportant}")
    print(f" ========= {r} {n} {d} {k} {ordreImportant} =========")
    os.system(f"echo {r} {n} {d} {k} {ordreImportant} | python TFJM-2021-Pb1.py")   