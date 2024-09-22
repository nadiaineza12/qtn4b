 a/b =  3
20 characters 
strcpy(email, "example@example.com");  cout << "Email: " << email << endl;
 cout << "inezanana1@gmail.com ";
cin >> email;  cout << "Your email is: " << email << endl;


#include <iostream>

using namespace std;

int main() {
    int grade;

    // Do-while loop to validate the grade input
    do {
        cout << "Enter your grade (0-100): ";
        cin >> grade;

        // Check if the input is valid
        if (grade < 0 || grade > 100) {
            cout << "Invalid input! Please enter a grade between 0 and 100." << endl;
        }

    } while (grade < 0 || grade > 100);

    cout << "Your grade is: " << grade << endl;

    return 0;
}
