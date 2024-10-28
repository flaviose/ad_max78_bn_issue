labels = ["rsz_this_fine.png", "rsz_fry.png", "rsz_grumpy_cat.png", "rsz_pikachu.png"]

f = open("./labels.txt", "w")
f.write(f"file_name,seq\n")
for i in range(500):
    for lab in enumerate(labels):
        f.write(f"{lab[1]},{lab[0]}\n")

f.close()