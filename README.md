# Armstrong-Number

Input: 1634

Output: Armstrong Number

Question Explanation:

The program aims to determine if a given four-digit number N is an Armstrong Number.

Armstrong Number:

An Armstrong Number is a number where the sum of its own digits, each raised to the power of the number of digits, equals the number itself.

Logical Approach:

Read Input:
Read the four-digit number N and store it as an integer.

Convert N to String and Find Number of Digits:
Convert N to a string to easily access each digit.
Find the number of digits in N (which is 4 for a four-digit number).

Calculate the Sum of Powers of Digits:
Initialize sum_of_powers to 0.
Loop through each digit in the string representation of N.
Convert each digit back to an integer and raise it to the power equal to the number of digits (4 in this case).
Add this value to sum_of_powers.

Check if N is an Armstrong Number:
Compare sum_of_powers with the original number N.
If they are equal, N is an Armstrong Number. Otherwise, it is not.

Output:
If N is an Armstrong Number, print "Armstrong Number".
Otherwise, print "Not an Armstrong Number".

Example for Clarity:

If the input N is 1634:
The digits in 1634 are 1, 6, 3, and 4.
The sum of their fourth powers is (1^4 + 6^4 + 3^4 + 4^4 = 1634), which is equal to the number itself.
Hence, 1634 is an Armstrong Number.
The output will be: Armstrong Number
