import random
import os
import time

R = [random.randint(0, 2 ** 32 - 1) for _ in range(256)]


def hash_crc(data: str):
    h = 0
    for ki in data:
        highorder = h & 0xf8000000
        h = h << 5
        h = h ^ (highorder >> 27)
        h = h ^ ki
    return h


def hash_pjw(data: str):
    h = 0
    for ki in data:
        h = (h << 4) + ki
        g = h & 0xf0000000
        if g != 0:
            h = h ^ (g >> 24)
            h = h ^ g
    return h


def hash_buz(data: str):
    h = 0
    for ki in data:
        highorder = h & 0x80000000
        h = h << 1
        h = h ^ (highorder >> 31)
        h = h ^ R[ki]
    return h


def hash_py(data: str):
    return hash(data)


def find_duplicates(files: list[str], hash_function: callable):
    start_time = time.time()
    hash_table = {}
    for file in files:
        file_path = os.path.join('out', file)
        with open(file_path, 'rb') as f:
            file_content = f.read()
            file_hash = hash_function(file_content)
            if file_hash in hash_table:
                hash_table[file_hash].append(file)
            else:
                hash_table[file_hash] = [file]
    duplicates = [files for files in hash_table.values() if len(files) > 1]
    end_time = time.time()
    return duplicates, end_time - start_time


print("FUNCTION\tDUPLICATES\tTIME")
duplicates_crc, time1 = find_duplicates(os.listdir('out'), hash_crc)
print("hash_crc\t", len(duplicates_crc), "\t", time1, "s")

duplicates_pjw, time2 = find_duplicates(os.listdir('out'), hash_pjw)
print("hash_pjw\t", len(duplicates_pjw), "\t", time2, "s")

duplicates_buz, time3 = find_duplicates(os.listdir('out'), hash_buz)
print("hash_buz\t", len(duplicates_buz), "\t", time3, "s")

duplicates_py, time4 = find_duplicates(os.listdir('out'), hash_py)
print("hash_py\t\t", len(duplicates_py), "\t", time4, "s")

