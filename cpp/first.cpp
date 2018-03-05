#include <iostream>
using namespace std;

void run();

class account{
		int amount;
	public:
		void start(){
			amount = 0;
		}

		void deposit(int value){
			amount += value;
		}

		void withdraw(int value){
			amount -= value;
		}

		int display(){
			return amount;
		}
};

int main(){

	run();

	return 0;
}


void run(void){
	int choice, value;

	account acc;
	acc.start();

	while(1){
		system("cls");
		cout << "What would you like to do?" << endl;
		cout << "1. Add funds" << endl << "2. Withdraw funds" << endl << "3. Display funds" << endl;

		cin >> choice;
	
		switch(choice){
			case 1:
				system("cls");
				cout << "How much would you like to add?" << endl << "Amount: ";
				cin >> value;
				cout << value;
				acc.deposit(value);
				break;
			case 2:
				cout << "dd" << endl;
				break;
			default:
				system("cls");
				cout << acc.display() << endl;
				cin >> value;
				break;
		}
	}
}
