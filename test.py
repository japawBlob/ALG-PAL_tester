import subprocess
import os

in_folder_path = "datapub"
out_folder_path = "datapub"

if __name__ == '__main__':
    command = ['wsl', './src/a.out']
    test_file_number = 1
    while (True):
        p = subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        i = str(test_file_number).zfill(2)
        test_file_in = os.path.join(in_folder_path, "pub" + i + ".in")
        test_file_out = os.path.join(in_folder_path, "pub" + i + ".out")
        try:
            with open(test_file_in, "r") as data_in:
                data = data_in.read()
                solution = p.communicate(input=bytes(data, encoding="UTF-8"))[0]
                retcode = p.wait()
                # print(solution, "\nreturn is", retcode)
                with open(test_file_out, "r") as data_out:
                    correct_out = data_out.read()
                # print("solution:", solution)
                # print("correct_out", bytes(correct_out, encoding="UTF-8"))
                try:
                    assert solution == bytes(correct_out, encoding="UTF-8")
                    print("solution for file ", test_file_number, " is OK")
                except AssertionError:
                    print("solutions for ", test_file_number, " don't match")
        except FileNotFoundError:
            break
        test_file_number += 1




