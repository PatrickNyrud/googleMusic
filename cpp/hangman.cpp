#include <iostream>
#include <string>
using namespace std;

bool checkIfRight(string, string);

int main(){
	system("cls");
	string guess;
	string word = "guess";
	bool done = false;
	int attempts = 1;

	cout << "Guess the word" << endl;

	while(! done){
		cin >> guess;
		if(checkIfRight(guess, word) == true){
			system("cls");
			done = true;
			cout << "You got it in " << attempts << " attempts!" << endl;
		} else{
			system("cls");
			cout << "Not right" << endl;
		}
		attempts++;
	}
	return 0;
}


bool checkIfRight(string guess, string word){
	if(guess == word){
		return true;
	}else if(guess != word){
		return false;
	}
}
