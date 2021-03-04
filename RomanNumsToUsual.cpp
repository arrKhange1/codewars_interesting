#include <iostream>
#include <string>
using namespace std;      // MCMXC = 1990 èäåì ñ êîíöà ñîáèðàÿ âñå

void solve()
{
	string str = "MCMXC";
	int* str_arr = new int[str.size()];
	for (int i = 0; i < str.size(); ++i)
	{
		if (str[i] == 'I') str_arr[i] = 1;
		else if (str[i] == 'V') str_arr[i] = 5;
		else if (str[i] == 'X') str_arr[i] = 10;
		else if (str[i] == 'L') str_arr[i] = 50;
		else if (str[i] == 'C') str_arr[i] = 100;
		else if (str[i] == 'D') str_arr[i] = 500;
		else if (str[i] == 'M') str_arr[i] = 1000;
		
	}
	for (int i = 0; i < str.size(); ++i)
	{
		cout << str_arr[i] << endl;
	}
	
	int res = str_arr[str.size()-1];
	
	for (int i = str.size() - 2; i >= 0; --i)
	{
		if (str[i] == str[i+1]) res += str_arr[i];
		else if (res <= str_arr[i]) res += str_arr[i];
		else if (res > str_arr[i]) res -= str_arr[i];
	}
	cout << endl << res << endl;
}

int main()
{
	solve();
	return 0;
}
