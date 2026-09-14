Answer the following questions. The question text is bold, your answer should
follow and be non-bold.

For each question, show the steps and then give your final answer.

**Question 0: (Example) Convert the decimal number 6.25 to binary.**

First the whole part, 6, using repeated division:

- 6 / 2 = 3 remainder 0
- 3 / 2 = 1 remainder 1
- 1 / 2 = 0 remainder 1

Take the remainders in reverse order: 110.

Then the fractional part, 0.25, using repeated multiplication:

- 0.25 * 2 = 0.5, digit 0
- 0.5 * 2 = 1.0, digit 1

Take the digits in order: .01

Answer: 110.01

**Question 1: Convert the decimal number 29 to binary using repeated division.**
29/2 =14 r 1
14/2=7 r   0
7/2=3 r    1
3/2=1 r    1
1/2=0 r    1
11101
**Question 2: Convert the decimal number 29 to hexadecimal.**
29-16=13
13= d
answer is 1d
**Question 3: Convert the binary number 1101101 to decimal.**
1   1
2   0
4   1
8   1
16  0
32  1
64  1
128
64+32+8+4+1=109
**Question 4: Convert the hexadecimal number C3 to binary.**
c=12
c=1100
3=11
c3=11000011
*For the next few questions, recall two's complement. With a fixed number of
bits, a negative value is represented by flipping every bit of the positive
value and then adding 1. For example, -2 in 4 bits is: +2 = 0010, flip to
1101, add 1 to get 1110.*

**Question 5: Convert the decimal number -6 into 4-bit two's complement binary.**
0110 positive
1001
 1010 negative

**Question 6: The 4-bit two's complement number 1101 represents which decimal
number?**
1101
sub1
 1
1100
-3
**Question 7: Convert the decimal number -25 into 8-bit two's complement
binary.**
100110
then add one
11100111
**Question 8: In 4-bit two's complement, the pattern 1000 is the smallest value
and 0111 is the largest. What decimal values are they?**
smalles is -8
biggest is 7
**Question 9: Convert the binary number 101.101 to decimal.**
5.625
**Question 10: Convert the decimal number 0.375 to binary using repeated
multiplication.**
.375*2= 0
.75*2= 1
.5*2=  1
.011
**Question 11: Convert the decimal number 47.25 to hexadecimal. To get the
fractional digits, repeatedly multiply the fractional part by 16.**
2f.4

*For the last questions, use the single-precision IEEE 754 layout: 1 sign bit,
8 exponent bits (biased, so the stored exponent is the real exponent plus 127),
and 23 fraction bits. The mantissa has an implicit leading 1, so the value is
+/-1.fraction times 2 to the (stored exponent - 127). For example, the pattern
0 01111111 00000000000000000000000 has stored exponent 127 and fraction 0, so
it represents 1.0 x 2^0 = 1.0.*

**Question 12: Encode the decimal number 6.5 as a single-precision IEEE 754
value. Give your answer as 32 bits, with spaces between the sign, exponent, and
fraction fields.**
110.1
1.101 x^2
remove the 1
.101
0 10000001 10100000000000000000000

**Question 13: Decode the single-precision IEEE 754 value
1 10000010 10000000000000000000000 to decimal.**
-1    exp3    1.1x2^3
1.1
1100
=
-12
**Question 14: Decode the single-precision IEEE 754 value
0 01111110 00000000000000000000000 to decimal.**
   exp-1     imp1
.5
**Question 15: Encode the decimal number 20.5 as a single-precision IEEE 754
value, again giving the full 32 bits with spaces between the fields.**
10100.1
1.01001 x2^4
remove the 1
.01001
4+127=131
0 10000011 01001000000000000000000
