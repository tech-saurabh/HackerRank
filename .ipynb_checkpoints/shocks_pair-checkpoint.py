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
      "5\n",
      "1 1 2 1 2\n",
      "the number of pairs of shocks are :  2\n"
     ]
    }
   ],
   "source": [
    "n = int(input())\n",
    "ar = list(map(int,input().split()))\n",
    "list2 = set(ar)\n",
    "list3=[]\n",
    "for i in list2:\n",
    "    list3.append(ar.count(i))   \n",
    "sum=0\n",
    "for i in list3:\n",
    "    sum=sum+(i//2)   \n",
    "  \n",
    "print(\"the number of pairs of shocks are : \",sum)"
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
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
