{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'int'>\n",
      "4527741568\n"
     ]
    }
   ],
   "source": [
    "# Q.Declare an int value and store it in a variable.\n",
    "a = 10\n",
    "\n",
    "# Check the type and print the id of the same\n",
    "print(type(a))\n",
    "print(id(a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4527744448\n",
      "4527744448\n"
     ]
    }
   ],
   "source": [
    "# Q.Take one int value between 0 - 256.Assign it to two different variables. \n",
    "b = 100\n",
    "c = 100\n",
    "    \n",
    "# Check the id of both the variables. \n",
    "print(id(b))\n",
    "print(id(c))\n",
    "\n",
    "# It should come same. Check why?\n",
    "# The id is same as value 100 is the object and as same object is assigned to both variables b and c,\n",
    "# hence both are stored at same address.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "140549978917776\n",
      "140549978918256\n"
     ]
    }
   ],
   "source": [
    "# Q.Take one int value either less than -5 or greater than 256.\n",
    "# Assign it to two different variables. \n",
    "d = -10\n",
    "e = -10\n",
    "\n",
    "# Check the id of both the variables. \n",
    "print(id(d))\n",
    "print(id(e))\n",
    "\n",
    "# It should come different. Check Why?\n",
    "# It's because of optimization technique in Python"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n",
      "2\n",
      "8\n",
      "2.0\n",
      "0\n",
      "2\n",
      "16\n"
     ]
    }
   ],
   "source": [
    "# Q.Arithmetic Operations on integers \n",
    "# Take two different integer values.Store them in two different variables. \n",
    "armtc1 = 4\n",
    "armtc2 = 2\n",
    "\n",
    "# Do below operations on them:-\n",
    "# Find sum of both numbers\n",
    "armtc_sum = armtc1+armtc2\n",
    "print(armtc_sum)\n",
    "\n",
    "# Find difference between them\n",
    "armtc_diff = armtc1-armtc2\n",
    "print(armtc_diff)\n",
    "\n",
    "# Find the product of both numbers.\n",
    "armtc_prd = armtc1*armtc2\n",
    "print(armtc_prd)\n",
    "\n",
    "# Find value after dividing first num with second number.\n",
    "armtc_div = armtc1/armtc2\n",
    "print(armtc_div)\n",
    "\n",
    "# Find the remainder after dividing first number with second number.\n",
    "armtc_mod = armtc1%armtc2\n",
    "print(armtc_mod)\n",
    "\n",
    "# Find the quotient after dividing first number with second number.\n",
    "armtc_qtnt = armtc1//armtc2\n",
    "print(armtc_qtnt)\n",
    "\n",
    "# Find the result of the first num to the power of the second number.\n",
    "armtc_exp = armtc1**armtc2\n",
    "print(armtc_exp)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "True\n",
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "# Q.Comparison Operators on integers \n",
    "# Take two different integer values. Store them in two different variables. \n",
    "cmpr_op1 = 15\n",
    "cmpr_op2 = 25\n",
    "\n",
    "# Do below operations on them:-\n",
    "# Compare these two numbers with below operator:- \n",
    "\n",
    "# Greater than, '>'\n",
    "cmpr_op = cmpr_op1 > cmpr_op2\n",
    "print(cmpr_op)\n",
    "\n",
    "# Smaller than, '<'\n",
    "cmpr_op = cmpr_op1 < cmpr_op2\n",
    "print(cmpr_op)\n",
    "\n",
    "# Greater than or equal to, '>='\n",
    "cmpr_op = cmpr_op1 >= cmpr_op2\n",
    "print(cmpr_op)\n",
    "\n",
    "# Less than or equal to, '<='\n",
    "cmpr_op = cmpr_op1 <= cmpr_op2\n",
    "print(cmpr_op)\n",
    "\n",
    "# Observe their output(return type should be boolean)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "True\n",
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "# Q.Equality Operator\n",
    "# Take two different integer values.Store them in two different variables.\n",
    "eq_op1 = 5\n",
    "eq_op2 = 15\n",
    "\n",
    "# Equate them using equality operators (==, !=) Observe the output(return type should be boolean)\n",
    "print(eq_op1 == eq_op2)\n",
    "print(eq_op1+10 == eq_op2)\n",
    "print(eq_op1 != eq_op2)\n",
    "print(eq_op1 != eq_op2-10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20\n",
      "0\n",
      "0\n",
      "0\n",
      "10\n",
      "20\n",
      "20\n",
      "0\n",
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "# Q.Logical operators\n",
    "# Observe the output of below code\n",
    "# Cross check the output manually\n",
    "\n",
    "print(10 and 20) #----------------------------------------->Output is 20 \n",
    "\n",
    "print(0 and 20)  #----------------------------------------->Output is 0 \n",
    "\n",
    "print(20 and 0)  #----------------------------------------->Output is 0 \n",
    "\n",
    "print(0 and 0)   #----------------------------------------->Output is 0\n",
    "\n",
    "print(10 or 20)  #----------------------------------------->Output is 10 \n",
    "\n",
    "print(0 or 20)   #----------------------------------------->Output is 20 \n",
    "\n",
    "print(20 or 0)   #----------------------------------------->Output is 20 \n",
    "\n",
    "print(0 or 0)    #----------------------------------------->Output is 0\n",
    "\n",
    "print(not 10)    #----------------------------------------->Output is False \n",
    "\n",
    "print(not 0)     #----------------------------------------->Output is True\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0b1010\n",
      "0b10100\n",
      "0\n",
      "0\n",
      "30\n",
      "30\n",
      "30\n",
      "30\n",
      "-11\n",
      "-11\n",
      "40\n",
      "40\n",
      "2\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "# Q.Bitwise Operators\n",
    "# Do below operations on the values provided below:-\n",
    "# Bitwise and(&) -----------------------------------------> 10, 20 -------> Output is 0\n",
    "print(bin(10))\n",
    "print(bin(20))\n",
    "\n",
    "print(10&20)\n",
    "print(0b00000)\n",
    "#10 --> 0b01010\n",
    "#20 --> 0b10100\n",
    "#---------------\n",
    "#&  --> 0b00000\n",
    "\n",
    "# Bitwise or(|) -----------------------------------------> 10, 20 -------> Output is 30\n",
    "print(10|20)\n",
    "print(0b11110)\n",
    "#10 --> 0b01010\n",
    "#20 --> 0b10100\n",
    "#---------------\n",
    "#|  --> 0b11110\n",
    "\n",
    "\n",
    "# Bitwise(^) -----------------------------------------> 10, 20 -------> Output is 30\n",
    "print(10^20)\n",
    "print(0b11110)\n",
    "#10 --> 0b01010\n",
    "#20 --> 0b10100\n",
    "#---------------\n",
    "#^  --> 0b11110\n",
    "\n",
    "#Bitwise negation(~) ------------------------------------> 10-------> Output is -11\n",
    "print(~10)\n",
    "print(-(10+1))\n",
    "\n",
    "# Bitwise left shift ------------------------------------> 10,2-------> Output is 40\n",
    "# print(bin(10)) --> 0000000000000000000000000b1010 --> 00000000000000000000000b101000 --> 0b101000 \n",
    "print(10<<2)\n",
    "print(0b101000)\n",
    "\n",
    "\n",
    "# Bitwise right shift ------------------------------------> 10,2 -------> Output is 2\n",
    "# print(bin(10)) --> 0000000000000000000000000b1010 --> 000000000000000000000000000b10 --> 0b10\n",
    "print(10>>2)\n",
    "print(0b10)\n",
    "\n",
    "# Cross check the output manually"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4527741568\n",
      "4527741568\n",
      "True\n",
      "False\n",
      "140549978197520\n",
      "140549978196656\n",
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "# Q.What is the output of expression inside print statement. Cross check before running the program.\n",
    "a = 10\n",
    "b = 10\n",
    "print(id(a))\n",
    "print(id(b))\n",
    "print(a is b) #True or False?\n",
    "# id is same so True\n",
    "\n",
    "print(a is not b) #True or False?\n",
    "# id is same so False\n",
    "\n",
    "a = 1000\n",
    "b = 1000\n",
    "print(id(a))\n",
    "print(id(b))\n",
    "print(a is b) #True or False?\n",
    "# id is not same so False\n",
    "\n",
    "print(a is not b) #True or False?\n",
    "# id is not same so True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20\n",
      "20\n",
      "116\n",
      "320\n",
      "32\n",
      "10\n",
      "20\n",
      "9\n",
      "29\n",
      "116\n",
      "20\n",
      "20\n"
     ]
    }
   ],
   "source": [
    "# Q.What is the output of expression inside print statement. Cross check before running the program.\n",
    "print(10+(10*32)//2**5&20+(~(-10))<<2)\n",
    "print(10+(10*32)//2**5)\n",
    "print(20+(~(-10))<<2)\n",
    "\n",
    "print(10*32)   #320\n",
    "print(2**5)    #32\n",
    "print(320//32) #10\n",
    "print(10+10)   #20\n",
    "\n",
    "print(~(-10)) # -(-10+1)= 9\n",
    "print(20+9)\n",
    "print(29<<2)   # bin(29)-->00000000000000000000000000b11101-->000000000000000000000000b1110100 --> 0b1110100 -->116\n",
    "\n",
    "print(20&116)\n",
    "print(0b0010100)\n",
    "#20  --> 0b0010100\n",
    "#116 --> 0b1110100\n",
    "#-----------------\n",
    "#&  --> 0b0010100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "True\n",
      "True\n",
      "True\n",
      "True\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "# Q.Membership operation\n",
    "# in, not in are two membership operators and it returns boolean value\n",
    "\n",
    "print('2' in 'Python2.7.8')\n",
    "print(10 in [10,10.20,10+20j,'Python']) \n",
    "print(10 in (10,10.20,10+20j,'Python')) \n",
    "print(2 in {1,2,3})\n",
    "print(3 in {1:100, 2:200, 3:300}) \n",
    "print(10 in range(20))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12\n",
      "584\n",
      "256\n",
      "0b10011010010100\n",
      "0o23224\n",
      "0x2694\n"
     ]
    }
   ],
   "source": [
    "# Q.An integer can be represented in binary, octal or hexadecimal form. \n",
    "# Declare one binary, one octal and one hexadecimal value and store them in three different variables.\n",
    "# Convert 9876 to its binary, octal and hexadecimal equivalent and print their corresponding value.\n",
    "\n",
    "bin_var = 0b1100\n",
    "print(bin_var)\n",
    "\n",
    "oct_var = 0o1110\n",
    "print(oct_var)\n",
    "\n",
    "hex_var = 0x00100\n",
    "print(hex_var)\n",
    "\n",
    "print(bin(9876))\n",
    "print(oct(9876))\n",
    "print(hex(9876))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "80\n",
      "3870\n",
      "64222\n",
      "0b1010000\n",
      "0o7436\n",
      "0xfade\n",
      "0b1010000\n",
      "0b1111101011011110\n",
      "0o175336\n",
      "0o7436\n",
      "0x50\n",
      "0xfade\n"
     ]
    }
   ],
   "source": [
    "# Q.What will be the output of following:- \n",
    "a = 0b1010000\n",
    "print(a)\n",
    "\n",
    "b = 0o7436 \n",
    "print(b)\n",
    "\n",
    "c = 0xfade \n",
    "print(c)\n",
    "\n",
    "print(bin(80))\n",
    "print(oct(3870)) \n",
    "print(hex(64222)) \n",
    "print(bin(0b1010000)) \n",
    "print(bin(0xfade)) \n",
    "print(oct(0xfade)) \n",
    "print(oct(0o7436)) \n",
    "print(hex(0b1010000)) \n",
    "print(hex(0xfade))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
