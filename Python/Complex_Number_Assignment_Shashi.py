{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'complex'>\n",
      "140611540004976\n"
     ]
    }
   ],
   "source": [
    "# Q.Declare a complex number and store it in a variable. Check the type and print the id of the same.\n",
    "a=10\n",
    "cmplx_num = a+5j\n",
    "\n",
    "print(type(cmplx_num))\n",
    "print(id(cmplx_num))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(20+12j)\n",
      "-8j\n",
      "(80+120j)\n",
      "(0.6-0.4j)\n",
      "(1686636955.5445778+106684882.4940285j)\n"
     ]
    }
   ],
   "source": [
    "# Q.Arithmetic Operations on complex number Take two different complex numbers.\n",
    "# Store them in two different variables.\n",
    "a=10\n",
    "\n",
    "cmplx_num1 = a+2j\n",
    "cmplx_num2 = a+10j\n",
    "\n",
    "# Do below operations on them:-\n",
    "# Find sum of both numbers\n",
    "print(cmplx_num1 + cmplx_num2)\n",
    "\n",
    "# Find difference between them\n",
    "print(cmplx_num1 - cmplx_num2)\n",
    "\n",
    "# Find the product of both numbers.\n",
    "print(cmplx_num1 * cmplx_num2)\n",
    "\n",
    "# Find value after dividing first num with second number\n",
    "print(cmplx_num1 / cmplx_num2)\n",
    "\n",
    "# Find the result of the first num to the power of the second number.\n",
    "print(cmplx_num1 ** cmplx_num2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Q.Comparison Operation not applicable between instance of complex values.\n",
    "# Object reusability concept is not applicable on complex number"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
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
    "# Take two different complex numbers.\n",
    "# Store them in two different variables.\n",
    "\n",
    "a = 5\n",
    "eq_op1 = a+2j\n",
    "eq_op2 = a+5j\n",
    "\n",
    "# Equate them using equality operators (==, !=) \n",
    "print(eq_op1 == eq_op2)\n",
    "print(eq_op1+(0+3j) == eq_op2)\n",
    "\n",
    "# Observe the output(return type should be boolean)\n",
    "print(eq_op1 != eq_op2)\n",
    "print(eq_op1+(0+3j) != eq_op2)"
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
      "(20+30j)\n",
      "0j\n",
      "0j\n",
      "0j\n",
      "(10+20j)\n",
      "(20+30j)\n",
      "(20+30j)\n",
      "0j\n",
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "# Q.Logical operators\n",
    "# Observe the output of below code Cross check the output manually\n",
    "\n",
    "print(10+20j and 20+30j) #20+30j\n",
    "\n",
    "print(0+0j and 20+30j) #0+0j\n",
    "\n",
    "print(20+30j and 0+0j) #0+0j\n",
    "\n",
    "print(0+0j and 0+0j) #0+0j\n",
    "\n",
    "print(10+20j or 20+30j) #10+20j\n",
    "\n",
    "print(0+0j or 20+30j) #20+30j\n",
    "\n",
    "print(20+30j or 0+0j) #20+30j\n",
    "\n",
    "print(0+0j or 0+0j) #0+0j\n",
    "\n",
    "print(not 10+20j) #False\n",
    "\n",
    "print(not 0+0j) #True"
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
      "140611540005264\n",
      "140611540005456\n",
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "# Q.What is the output of the expression inside the print statement. Cross check before running the program.\n",
    "a = 10+20j\n",
    "b = 10+20j\n",
    "\n",
    "print(id(a))\n",
    "print(id(b))\n",
    "print(a is b) #False #True or False? \n",
    "print(a is not b) #True #True or False?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
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
    "print('2.7' in 'Python2.7.8')\n",
    "print(10+20j in [10,10.20,10+20j,'Python']) \n",
    "print(10+20j in (10,10.20,10+20j,'Python')) \n",
    "print(30+40j in {1,20.30,30+40j}) \n",
    "print(30+40j in {1:100, 2.3:200, 30+40j:300}) \n",
    "print(10+0j in range(20))"
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
