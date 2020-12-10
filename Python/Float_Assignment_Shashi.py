{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'float'>\n",
      "140522745899632\n"
     ]
    }
   ],
   "source": [
    "# Q.Declare a float value and store it in a variable. \n",
    "a = 10.2\n",
    "\n",
    "#Check the type and print the id of the same.\n",
    "print(type(a))\n",
    "print(id(a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "26.1\n",
      "5.1\n",
      "163.79999999999998\n",
      "1.4857142857142858\n",
      "5.1\n",
      "1.0\n",
      "3371384476053.723\n"
     ]
    }
   ],
   "source": [
    "# Q.Arithmetic Operations on float Take two different float values.\n",
    "# Store them in two different variables. \n",
    "armtc1 = 15.6\n",
    "armtc2 = 10.5\n",
    "\n",
    "# Do below operations on them:-\n",
    "# Find sum of both numbers\n",
    "print(armtc1+armtc2)\n",
    "\n",
    "# Find difference between them\n",
    "print(armtc1-armtc2)\n",
    "\n",
    "# Find the product of both numbers.\n",
    "print(armtc1*armtc2)\n",
    "\n",
    "# Find value after dividing first num with second number\n",
    "print(armtc1/armtc2)\n",
    "\n",
    "# Find the remainder after dividing first number with second number\n",
    "print(armtc1%armtc2)\n",
    "\n",
    "#Find the quotient after dividing first number with second number\n",
    "print(armtc1//armtc2)\n",
    "\n",
    "#Find the result of the first num to the power of the second number.\n",
    "print(armtc1**armtc2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n",
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "# Q.Comparison Operators on float\n",
    "# Take two different float values.\n",
    "# Store them in two different variables. \n",
    "comp_op1 = 20.5\n",
    "comp_op2 = 10.5\n",
    "\n",
    "# Do below operations on them:-\n",
    "# Compare these two numbers with below operator:- \n",
    "\n",
    "# Greater than, '>'\n",
    "print(comp_op1>comp_op2)\n",
    "\n",
    "# Smaller than, '<'\n",
    "print(comp_op1<comp_op2)\n",
    "\n",
    "# Greater than or equal to, '>=' \n",
    "print(comp_op1>=comp_op2)\n",
    "\n",
    "#Less than or equal to, '<='\n",
    "print(comp_op1<=comp_op2)\n",
    "\n",
    "# Observe their output(return type should be boolean)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "# Q.Equality Operator\n",
    "# Take two different float values.\n",
    "# Store them in two different variables.\n",
    "eq_op1 = 30.5\n",
    "eq_op2 = 30.5\n",
    "\n",
    "# Equate them using equality operators (==, !=) \n",
    "print(eq_op1==eq_op2)\n",
    "print(eq_op1!=eq_op2)\n",
    "\n",
    "# Observe the output(return type should be boolean)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20.3\n",
      "0.0\n",
      "0.0\n",
      "0.0\n",
      "10.2\n",
      "20.3\n",
      "20.3\n",
      "0.0\n",
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "# Q.Logical operators\n",
    "# Observe the output of below code Cross check the output manually\n",
    "\n",
    "print(10.20 and 20.30) #both are true and second value taken >Output is 20.3\n",
    "\n",
    "print(0.0 and 20.30) #First is false so first value taken->Output is 0.0\n",
    "\n",
    "print(20.30 and 0.0) #Goes to till second and second value is false so second is taken>Output is 0.0\\\n",
    "\n",
    "print(0.0 and 0.0) #First is false so first value is taken->Output is 0.0\n",
    "  \n",
    "print(10.20 or 20.30 ) #First is True so first value is taken>Output is 10.2\n",
    "\n",
    "print(0.0 or 20.30) #Goes to till second and second is true second value is taken->Output is 20.3\n",
    "\n",
    "print(20.30 or 0.0) #First is True so first value is taken->Output is 20.3\n",
    "\n",
    "print(0.0 or 0.0) #Goes to till second and second is also false and second value is taken>Output is 0.0\n",
    "\n",
    "print(not 10.20) #-Not of true is false->Output is False \n",
    "\n",
    "print(not 0.0) #Not of false is True>Output is True"
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
      "False\n",
      "140522747129392\n",
      "140522747654992\n"
     ]
    }
   ],
   "source": [
    "# Q.What is the output of expression inside print statement. Cross check before running the program.\n",
    "a = 10.20\n",
    "b = 10.20\n",
    "\n",
    "print(a is b) #True or False? True 10.20<256 but, it's not integer. \n",
    "              #So, id will be different other than any value except integer -5 to 256\n",
    "print(a is not b) #True or False? False\n",
    "print(a.is_integer())\n",
    "print(b.is_integer())\n",
    "print(id(a))\n",
    "print(id(b))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# If the below is an integer and is within the range of -5 and 256 then why the result is different \n",
    "# than of an integer.\n",
    "c = 10.0\n",
    "d = 10.0\n",
    "print(c.is_integer())\n",
    "print(d.is_integer())\n",
    "print(c is d)\n",
    "print(c is not d)\n",
    "print(id(c))\n",
    "print(id(d))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "140522747129392\n",
      "140522745899632\n",
      "140522747129392\n",
      "140522747129392\n"
     ]
    }
   ],
   "source": [
    "# Q.Why the Id of float values are different when the same value is assigned to two different variables\n",
    "# ex: a = 10.5 b=10.5. but id will be same if I assign the variable having float i.e. a=c \n",
    "# then both a and c's Id are same\n",
    "a = 10.5 \n",
    "b = 10.5\n",
    "print(id(a))\n",
    "print(id(b))\n",
    "c = a\n",
    "print(id(c))\n",
    "print(id(a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
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
    "print('2.7' in 'Python2.7.8')\n",
    "\n",
    "print(10.20 in [10,10.20,10+20j,'Python']) \n",
    "\n",
    "print(10.20 in (10,10.20,10+20j,'Python')) \n",
    "\n",
    "print(20.30 in {1,20.30,30+40j}) \n",
    "\n",
    "print(2.3 in {1:100, 2.3:200, 30+40j:300}) \n",
    "\n",
    "print(10 in range(20))"
   ]
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
