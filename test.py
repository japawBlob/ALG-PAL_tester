import subprocess

if __name__ == '__main__':
    print('\n')
    command = ['wsl', './src/a.out']
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    out = p.communicate(input=bytes('hou there i am big boy', encoding="UTF-8"))[0]
    retcode = p.wait()
    print(out, "\nreturn is", retcode)

