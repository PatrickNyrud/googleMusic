#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool checkIfGuessed();
void checkGuess(char);

vector<char> rightWords;
vector<char> wordsGuessed;
string wordToGuess = "hello";

int main(){
	system("cls");
	char guess;
	bool done;

	while(!done){
		cin >> guess;
		system("cls");
		checkGuess(guess);

		if(checkIfGuessed()){
			done = true;
			system("cls");
			cout << "Youve won!" << endl;
		}
	}
	return 0;
}

bool checkIfGuessed(){
	int check = 0;

	for(int i = 0; i < rightWords.size(); i++){
		check++;
	}
	if(check == wordToGuess.length()){
		return true;
	}else{
		return false;
	}
}


void checkGuess(char guess){
	if(find(wordsGuessed.begin(), wordsGuessed.end(), guess) == wordsGuessed.end()){
		for(int i = 0; i < wordToGuess.length(); i++){
			if(wordToGuess[i] == guess){
				cout << "Youve guessed right" << endl;
				rightWords.push_back(guess);
			}else{
				cout << "Youve guessed wrong" << endl;
			}
		}	
		wordsGuessed.push_back(guess);
	}else{
		cout << "Youve guessed " << guess << endl;
	}
	cout << endl << "Letters youve guessed" << endl;
	for(int i = 0; i < wordsGuessed.size(); i++){
		cout << wordsGuessed[i];
	}
	cout << endl << endl << "Right wordsGuessed guessed" << endl;
	for(int i = 0; i < rightWords.size(); i++){
		cout << rightWords[i];
	}
}
