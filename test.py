#!/usr/bin/env python3

from platform import platform
import subprocess
import os
from unicodedata import name
import toml


class Tester:
    def __init__(self):
        print("hey")
        self.exe_name : str = ""
        self.language : str = ""
        self.platform : str = ""
        self.compilator : str = ""
        self.data_in : str = ""
        self.data_out : str = ""
        self.load_config()
        
   
    def load_config(self):
        config = toml.load("config.toml")
        # print(config["program"]["exe_name"])
        self.exe_name = config["program"]["exe_name"]
        self.language = config["program"]["language"]
        if config["program"]["platform"] == "wsl" or config["program"]["platform"] == "native":
            self.platform = config["program"]["platform"]
        else:
            print("Supported platforms are \"wsl\" and \"native\"")
            exit(1)
        self.compilator = config["program"]["compilator"]

        self.data_in = config["datapub_folder"]["in"]
        self.data_out = config["datapub_folder"]["out"]
                  
    def compile(self):
        pass   
    
    def run(self):
        if self.platform == "wsl":
            command = [self.platform, './src/' + self.exe_name]
        else: 
            command = ['./src/' + self.exe_name]
        test_file_number = 1
        while True:
            p = subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
            i = str(test_file_number).zfill(2)
            test_file_in = os.path.join(in_folder_path, "pub" + i + ".in")
            test_file_out = os.path.join(in_folder_path, "pub" + i + ".out")
            try:
                with open(test_file_in, "r") as data_in:
                    data = data_in.read()
                    solution = p.communicate(input=bytes(data, encoding="UTF-8"))[0]
                    retcode = p.wait()
                    with open(test_file_out, "r") as data_out:
                        correct_out = data_out.read()
                    try:
                        assert solution == bytes(correct_out, encoding="UTF-8")
                        print("solution for file ", test_file_number, " is OK")
                    except AssertionError:
                        print("solutions for ", test_file_number, " don't match")
            except FileNotFoundError:
                break
            test_file_number += 1
         
    def run_batch(self):
        pass
    
in_folder_path = "datapub"
out_folder_path = "datapub"

if __name__ == '__main__':
    blob = Tester()
    blob.run()
    




