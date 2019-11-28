
def soft_to_site(file, Items):
    with open(file + '.site', "w")as f:
        for item in Items:
            for i in item:
                f.write(i + " ")
            f.write("\n")
        f.close()
def site_to_soft(file):
    pass

