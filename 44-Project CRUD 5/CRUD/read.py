import database


def read(**kwargs):
    try:
        with open(database.DB_NAME, "r") as file:
            content = file.readlines()
            if "index" in kwargs:
                jumlah_siswa = len(content)
                index_siswa = kwargs["index"] - 1
                if index_siswa < -1 or index_siswa > jumlah_siswa:
                    return False
                else:
                    return content[index_siswa]
            else:
                return content
    except Exception as error_massage:
        print(error_massage)
        return False


def read_data():
    data_file = read()

    # Data
    for index, data in enumerate(data_file):
        data_break = data.split(",")
        key = data_break[0]
        nama = data_break[1]
        almt = data_break[2]
        tmp = data_break[3]
        tgl = data_break[4]
        print(f"{key:<6} {index+1:<3} {nama:<8} {almt:<10} {tmp:<14} {tgl:<10}", end="")
