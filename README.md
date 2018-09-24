# machine_learing_homework
1. Inspect the distribution of the amountAlcohol feature for each class and determine if it
follows a Gaussian or Exponential distribution. Record this result as a comment in
learnLambda.m or in hw1.py . Just write “Gaussian” or “Exponential” for each class.
You can inspect the distribution of value in a list/vector of numbers vector through a
histogram. In Matlab, use hist(vector) . 

In Python,
import matplotlib.pyplot as plt
plt.hist(vector)
plt.show()

Regardless of your answer for 1, let us now assume we want to learn an exponential likelihood
for each class. This means, we want to learn parameter 𝜆𝑦 for each of the three age classes.

2. Write a function called learnLambda that takes in a data set (with the format of the trainData
matrix) and a class number, and returns the learned mean amountAlcohol for that class. It turns
out the one divided by the mean feature value in the class is the best lambda parameter
estimate 𝜆𝑦 = 1/𝑚𝑒𝑎𝑛𝑦

Specifically, the function will be called as:
learnLambda(Data, classNum)
where Data is a matrix and classNum is a single number, the function will return a single
number. If you use Python, Data must be either a list or a numpy array.


3. Write a function called labelML that takes in an amountAlcohol measurement and a vector
containing the lambda values for the three shopper classes. labelML then will return the
Maximum Likelihood class for the input amountAlcohol measurement. Specifically, it will be
called as:
labelML(amountAlc, lambdas)
where amountAlc is a single number and lambdas is the list [𝜆𝑀𝑖𝑛𝑜𝑟, 𝜆𝑇𝑒𝑒𝑛, 𝜆𝐴𝑑𝑢𝑙𝑡]. The
function will return a single character, M, T, or A S, for the most likely class. For Python, the
vector lambdas must be either a list or a numpy array.
4. Write a function called learnPrior that takes in a data set (with the format of the trainData
matrix) and a class number, and returns the prior probability of the specified class. Specifically,
it will be called as:
learnPrior(Data, classNum) 
where Data is a matrix and classNum is a single number, the function will return a single
number. If you use Python, Data must be either a list or a numpy array.
