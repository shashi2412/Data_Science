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
      "<class 'bool'>\n",
      "4360743352\n"
     ]
    }
   ],
   "source": [
    "# Q.Declare a boolean value and store it in a variable. Check the type and print the id of the same.\n",
    "a = True\n",
    "\n",
    "print(type(a))\n",
    "print(id(a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Q.Take one boolean value between 0 - 256.\n",
    "# Assign it to two different variables.\n",
    "# Check the id of both the variables. It should come the same. Check why?\n",
    "\n",
    "bval1 = bool(0)\n",
    "bval2 = bool(10)\n",
    "bval3 = bool(2)\n",
    "\n",
    "print(bval1)\n",
    "print(bval2)\n",
    "print(bval3)\n",
    "print(id(bval1))\n",
    "print(id(bval2))\n",
    "print(id(bval3))\n",
    "\n",
    "# id for bval2 and bval3 are same as boolean variable always returns 0 or 1 in case of true\n",
    "# id for bval1 and bval2 are different as bval1 returns 0 and others return 1."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# I think it should be between 1 - 256."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "0\n",
      "1\n",
      "1.0\n",
      "0\n",
      "1\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "# Q.Arithmetic Operations on boolean data Take two different boolean values.\n",
    "# Store them in two different variables. Do below operations on them:-\n",
    "armtc1 = bool(20)\n",
    "armtc2 = bool(5)\n",
    "\n",
    "# Find sum of both values\n",
    "print(armtc1 + armtc2)    # 1+1\n",
    "\n",
    "# Find difference between them\n",
    "print(armtc1 - armtc2)   # 1-1\n",
    "\n",
    "# Find the product of both.\n",
    "print(armtc1 * armtc2)  # 1*1\n",
    "\n",
    "# Find value after dividing first value with second value\n",
    "print(armtc1 / armtc2) # 1/1\n",
    "\n",
    "# Find the remainder after dividing first value with second value \n",
    "print(armtc1 % armtc2) # 1%1\n",
    "\n",
    "# Find the quotient after dividing first value with second value \n",
    "print(armtc1 // armtc2) # 1//1\n",
    "\n",
    "# Find the result of first value to the power of second value.\n",
    "print(armtc1 ** armtc2) # 1**1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "True\n",
      "False\n",
      "True\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "# Q.Comparison Operators on boolean values Take two different boolean values.\n",
    "# Store them in two different variables.\n",
    "comp_op1 = bool(30)\n",
    "comp_op2 = bool(5)\n",
    "comp_op3 = bool(0)\n",
    "\n",
    "# Do below operations on them:-\n",
    "# Compare these two values with below operator:- \n",
    "# Greater than, '>'\n",
    "print(comp_op1 > comp_op2)\n",
    "print(comp_op1 > comp_op3)\n",
    "\n",
    "# less than, '<'\n",
    "print(comp_op1 < comp_op2)\n",
    "\n",
    "# Greater than or equal to, '>='\n",
    "print(comp_op1 >= comp_op2)\n",
    "\n",
    "# Less than or equal to, '<='\n",
    "print(comp_op1 <= comp_op2)\n",
    "\n",
    "# Observe their output(return type should be boolean)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "True\n",
      "False\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "# Q.Equality Operator\n",
    "# Take two different boolean values.\n",
    "# Store them in two different variables.\n",
    "eq_op1 = bool(10)\n",
    "eq_op2 = bool(2)\n",
    "eq_op3 = bool(0)\n",
    "\n",
    "# Equate them using equality operators (==, !=) \n",
    "print(eq_op1 == eq_op2)\n",
    "print(eq_op1-1 == eq_op3)\n",
    "\n",
    "# Observe the output(return type should be boolean)\n",
    "print(eq_op1 != eq_op2)\n",
    "print(eq_op1-1 != eq_op3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n",
      "False\n",
      "False\n",
      "True\n",
      "True\n",
      "True\n",
      "False\n",
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "# Q.Logical operators\n",
    "# Observe the output of below code Cross check the output manually\n",
    "\n",
    "print(True and True)#----------------------------------------->Output is True\n",
    "\n",
    "print(False and True) #----------------------------------------->Output is False\n",
    "\n",
    "print(True and False) #----------------------------------------->Output is False\n",
    "\n",
    "print(False and False) #----------------------------------------->Output is False\n",
    "\n",
    "print(True or True) #----------------------------------------->Output is True\n",
    "\n",
    "print(False or True) #----------------------------------------->Output is True\n",
    "\n",
    "print(True or False) #----------------------------------------->Output is True\n",
    "\n",
    "print(False or False) #----------------------------------------->Output is False\n",
    "\n",
    "print(not True) #----------------------------------------->Output is False\n",
    "\n",
    "print(not False) #----------------------------------------->Output is True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0b1\n",
      "0b0\n",
      "True\n",
      "True\n",
      "True\n",
      "-2\n",
      "-2\n",
      "4\n",
      "4\n",
      "0\n"
     ]
    }
   ],
   "source": [
    "# Q.Bitwise Operators\n",
    "# Do below operations on the values provided below:-\n",
    "print(bin(True)) # 0b1\n",
    "print(bin(False))# 0b0\n",
    "\n",
    "# Bitwise and(&) --------------> True, True \n",
    "#  0b1\n",
    "#  0b1\n",
    "#-----\n",
    "#& 0b1\n",
    "\n",
    "print(True & True)\n",
    "\n",
    "# Bitwise or(|) --------------> True, False \n",
    "#  0b1\n",
    "#  0b0\n",
    "#-----\n",
    "#| 0b1\n",
    "\n",
    "print(True | False)\n",
    "\n",
    "# Bitwise(^) --------------> True, False \n",
    "#  0b1\n",
    "#  0b0\n",
    "#-----\n",
    "#^ 0b1\n",
    "\n",
    "print(True ^ False)\n",
    "\n",
    "# Bitwise negation(~) ---------> True \n",
    "print(~True)  \n",
    "print(-(1+1))\n",
    "\n",
    "# Bitwise left shift ---------> True,2 \n",
    "print(True<<2) # 000000000000000000000000000000b1 --> 0000000000000000000000000000b100 --> 0b100\n",
    "print(0b100)\n",
    "\n",
    "# Bitwise right shift ---------> True,2\n",
    "# print(True>>2) # 000000000000000000000000000000b1 --> ?\n",
    "\n",
    "\n",
    "# Cross check the output manually"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Bitwise right shift ---------> True,2\n",
    "#print(True>>2) # 000000000000000000000000000000b1 --> ?\n",
    "\n",
    "# How this will work?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4360743352\n",
      "4360743352\n",
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "# Q.What is the output of expression inside the print statement. Cross check before running the program.\n",
    "a = True\n",
    "b = True\n",
    "\n",
    "print(id(a))\n",
    "print(id(b))\n",
    "print(a is b) #True or False?\n",
    "print(a is not b) #True or False? "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4360744088\n",
      "4360744088\n",
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "a = False\n",
    "b = False \n",
    "\n",
    "print(id(a))\n",
    "print(id(b))\n",
    "print(a is b) #True or False?\n",
    "print(a is not b) #True or False?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
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
      "True\n"
     ]
    }
   ],
   "source": [
    "# Q.Membership operation\n",
    "# in, not in are two membership operators and it returns boolean value\n",
    "print(True in [10,10.20,10+20j,'Python', True]) \n",
    "print(False in (10,10.20,10+20j,'Python', False)) \n",
    "print(True in {1,2,3, True})\n",
    "print(True in {True:100, False:200, True:300}) \n",
    "print(False in  {True:100, False:200, True:300})"
   ]
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
