#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool checkIfRight(string, string);
void runHangman(void);
void testFunc(void);

int main(){
	system("cls");
	
	testFunc();
	
	return 0;
}

void testFunc(void){
	vector<char> liste;
	bool done = false;
	char guess;

	while(! done){
		cin >> guess;
		if(find(liste.begin(), liste.end(), guess) != liste.end()){
			cout << "Youve guessed " << guess << endl;
		} else{
			liste.push_back(guess);
		}

		for(int i = 0; i < liste.size(); i++){
			cout << "at " << i << " is " << liste[i] << endl;
		}
	}
}

void runHangman(void){
	string guess;
	string word = "guess";
	bool done = false;
	int attempts = 1;

	cout << "Guess the word" << endl << "> ";

	while(! done){
		cin >> guess;
		if(checkIfRight(guess, word) == true){
			system("cls");
			done = true;
			cout << "You got it in " << attempts << " attempts!" << endl;
		} else{
			system("cls");
			cout << "Not right, guess again" << endl << "> ";
		}
		attempts++;
	}


}

bool checkIfRight(string guess, string word){
	if(guess == word){
		return true;
	}else if(guess != word){
		return false;
	}
}
