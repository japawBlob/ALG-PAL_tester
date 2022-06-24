#include "iostream"
#include <unistd.h>

using namespace std;


int main(int argc, char* argv []){
    if (argc > 1) {
        for (int i = 1; i<argc; i++){
            cout << argv[i] << endl;
        }
    }
    string line;
    getline(cin, line);
    sleep(2);
    cout << line << endl;
    return 0;
}