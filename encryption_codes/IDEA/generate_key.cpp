#include<bits/stdc++.h>
using namespace std;

int main()
{
	vector<int>key;

	ofstream myfile("key.txt");
	for(int i=0;i<16;i++) myfile << (rand() % 256) << "\n";
	return 0;
}