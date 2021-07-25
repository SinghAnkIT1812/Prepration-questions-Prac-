include <iostream>
#include <vector>
#include<utility>
using namespace std ;



int main() {
 int i ;
 int c = 0;

 int n , k ;

 cin>> n ; cin >> k ;

 vector<pair<int,int>>v ;
int j ;
    if ( n == 1 || k == 1 )
    {
        int temp ;
        temp = n>k?n:k;
        cout << temp<< endl ;
    }else {
        for (i = 1; i <= k+1; i++) {
            for (j = 1; j <= n; j++) {
                pair<int, int> p = make_pair(i, j);
                v.push_back(p);
            }

        }

        for (auto it : v) {
           
            if ( it.second % it.first == 0  )
            {

                c++ ;
            }

        }
    }
    if (c) {
        cout << c << endl;
    }
 return 0 ;
}