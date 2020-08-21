#include <iostream>
#include <string>
#include <algorithm>

using std::string;
using std::cout;
using std::endl;

namespace {

int s_nStep;

void MoveItem (int n, string strFrom, string strTo)
{
    ++s_nStep;
    cout << "Step[" << s_nStep << "] Move " << n << " from " << strFrom << " to " << 
        strTo << endl;
    return ; 
}

void Hanoi (int n, string strFrom, string strMid, string strTo)
{
    if (1 == n)
    {
        MoveItem (1, strFrom, strTo);
    }
    else 
    {
        Hanoi (n-1, strFrom, strTo, strMid);
        MoveItem (n, strFrom, strTo);
        Hanoi (n-1, strMid, strFrom, strTo);
    }
    return ;
}

}


int main()
{
    Hanoi (3, "A", "B", "C");
    return 0;
}