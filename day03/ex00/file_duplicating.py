from bs4 import BeautifulSoup


def file_duplicate_by_data(src, dest):
    # fp1 = open(src_file_path, "r")
    # fp2 = open(dest, "w")

    # data = fp1.readlines()
    # fp2.writelines(data)

    # fp1.close()
    # fp2.close()

    with open(src, "r") as fp1:
        with open(dest, "w") as fp2:
            data = fp1.readlines()
            fp2.writelines(data)


def file_duplicate_by_soup(src, dest):
    # fp1 = open(src, "r")
    # fp2 = open(dest, "w")

    # soup = BeautifulSoup(fp1, "lxml")
    # fp2.write(str(soup.prettify()))

    # fp1.close()
    # fp2.close()

    with open(src, "r") as fp1:
        with open(dest, "w") as fp2:
            soup = BeautifulSoup(fp1, "lxml")
            fp2.write(str(soup.prettify()))


if __name__ == "__main__":
    src_file_path = "../../materials/evilcorp.html"
    dest_file_path = "../../materials/evilcorp_hacked.html"
    # file_duplicate_by_data(src_file_path, dest_file_path)
    file_duplicate_by_soup(src_file_path, dest_file_path)
