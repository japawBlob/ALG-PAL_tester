# ALG-PAL_tester
Basic python script for testing your datapub inputs on your hw implementation

## Follow these steps to use this tester:

1. Paste your executable into the /src folder (compiling by tester is not implemented yet)
2. Fill out config.toml with details abour your program
3. Run tester and marvel at results!

<span style="color:red">**WARNING**</span>: The tester looks for exact match, so before panicking - try to run the test yourself and see the output. Maybe your program runs fine, just whitespaces don't match.

## Currently supported:  
 - Testing all pub inputs with outputs. And displaying result. 
 - If you create additional pubXX.in and pubXX.out files and name them  accordingly (according being pub number +1 from the previous max), the script will automatically test them.

## What I would like to implement in future (no guarantee it will ever be implemented)
 - Testing individual pub file.
 - Displaying what exactly didn't match.
 - Using multiple threads to run tests more quickly.
 - Compiling program with tester.
 - Multi language support
 - Testing on docker instance