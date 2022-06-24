import subprocess

if __name__ == '__main__':
    command = ['wsl', './src/a.out']
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    with open("datapub/pub01.in", "r") as data_in:
        data = data_in.read()
        solution = p.communicate(input=bytes(data, encoding="UTF-8"))[0]
        retcode = p.wait()
        print(solution, "\nreturn is", retcode)
        with open("datapub/pub01.out", "r") as data_out:
            correct_out = data_out.read()
        # print("solution:", solution)
        # print("correct_out", bytes(correct_out, encoding="UTF-8"))
        assert solution == bytes(correct_out, encoding="UTF-8")


