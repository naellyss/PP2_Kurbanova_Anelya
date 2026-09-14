#include <iostream> 
#include <algorithm> 
#include <utility>
using namespace std;

long long gcd(long long a, long long b){
        
        while (b != 0){
            int rem = a % b;
            a = b;
            b = rem;

            
            
        }
        return a;
    }

int main() {
    long long a;
    long long b;
    cin >> a >> b;

    int result = gcd(a, b);

    cout << result << endl;


    return 0;
}