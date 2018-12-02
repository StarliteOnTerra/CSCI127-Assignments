#include <iostream>

int main() {
    int userNumber;
    std::cout << "Enter an integer value between 0 and 99: ";
    std::cin >> userNumber;
    int guess;
    while(guess <= 99) {
    	int i = rand() % 100; /* between 0 and 99 */
    	std::cout << i;
    	std::cout << " is this correct?";

    	int number_1;
    	int number_2;
    	int number_3;
    		if(guess < userNumber) { std::cin >> number_1; } 
    		if(guess > userNumber) { std::cin >> number_2; }
    		if(guess == userNumber) { std::cin >> number_3; std::cout << "This is correct."; }
    }
    return 0;
}


