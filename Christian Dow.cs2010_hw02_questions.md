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

**Question 2: Convert the decimal number 29 to hexadecimal.**

**Question 3: Convert the binary number 1101101 to decimal.**

**Question 4: Convert the hexadecimal number C3 to binary.**

*For the next few questions, recall two's complement. With a fixed number of
bits, a negative value is represented by flipping every bit of the positive
value and then adding 1. For example, -2 in 4 bits is: +2 = 0010, flip to
1101, add 1 to get 1110.*

**Question 5: Convert the decimal number -6 into 4-bit two's complement binary.**

**Question 6: The 4-bit two's complement number 1101 represents which decimal
number?**

**Question 7: Convert the decimal number -25 into 8-bit two's complement
binary.**

**Question 8: In 4-bit two's complement, the pattern 1000 is the smallest value
and 0111 is the largest. What decimal values are they?**

**Question 9: Convert the binary number 101.101 to decimal.**

**Question 10: Convert the decimal number 0.375 to binary using repeated
multiplication.**

**Question 11: Convert the decimal number 47.25 to hexadecimal. To get the
fractional digits, repeatedly multiply the fractional part by 16.**

*For the last questions, use the single-precision IEEE 754 layout: 1 sign bit,
8 exponent bits (biased, so the stored exponent is the real exponent plus 127),
and 23 fraction bits. The mantissa has an implicit leading 1, so the value is
+/-1.fraction times 2 to the (stored exponent - 127). For example, the pattern
0 01111111 00000000000000000000000 has stored exponent 127 and fraction 0, so
it represents 1.0 x 2^0 = 1.0.*

**Question 12: Encode the decimal number 6.5 as a single-precision IEEE 754
value. Give your answer as 32 bits, with spaces between the sign, exponent, and
fraction fields.**

**Question 13: Decode the single-precision IEEE 754 value
1 10000010 10000000000000000000000 to decimal.**

**Question 14: Decode the single-precision IEEE 754 value
0 01111110 00000000000000000000000 to decimal.**

**Question 15: Encode the decimal number 20.5 as a single-precision IEEE 754
value, again giving the full 32 bits with spaces between the fields.**
