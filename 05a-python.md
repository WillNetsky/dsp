# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

> Tuples and lists are both objects that contain a sequence of values. They can both have their individual elements
accessed with index notation (square brackets with the index number(s)). There are a few differences, however. Lists are  
mutable, meaning that their value can change in place. Tuples are immutable, meaning they are static once created.  
In Python, assignment is not mutation. This means that you can still change the value of a tuple, you just have to  
reassign it. For example, there are no built-in functions to append an item to a tuple, the way there is for a list.  
  
> Tuples can be used as keys in dictionaries, while lists cannot. This is because, in Python, a dictionary key must  
be hashable. An object is considered hashable if it has a hash value that never changes in its lifetime. This means  
that all immutable Python types can be used as dictionary keys, while immutable types cannot.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

> Lists are sequences and can be indexed or sliced, whereas sets are an unordered collection of elements. Sets are useful in  
situations where a set operation (checking whether a set is a subset of another, set differences, etc) would be used. Lists  
are better in situations where iteration is necessary. In terms of finding a specific element, sets are faster because of their  
use of hashes rather than index to access elements.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

> Lambda is a Python statement that is  used to create an anonymous function. It essentially creates functions the same way  
that `def` does. In fact, the following two function declarations are equivalent:
```python
def square_root(x): return math.sqrt(x)
square_root = lambda x: math.sqrt(x)
```  
Lambda is limited by the fact that it can only accept one expression as a function. However, it is still extremely useful for  
creating one-off functions, and for functions as an argument in the `map` and `filter` functions.  
Here's an example of using lambda for the `key` argument in `sorted`:
```python
sorted(tuples, key = lambda t: t[-1])
```
This expression takes a list of tuples (called tuples) and sets the key of the sorted function to be a lambda function.  
The lambda function returns the last element of each individual tuple. Sorted then takes this key and sorts the list of tuples  
by this value.

--------

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

> List comprehensions are, simply put, a way to transform a list (or any iterable) into another. They use a syntax that is  
similar to that which would be used by mathematicians. List comprehensions consist of an input list, a variable  
that represents from that input list, an outputted expression and an optional predicate (that can be used to  
filter the original list).  
Many list comprehensions can be represented by an equivalent series of `map` and `filter` calls. Here's an example that takes  
each element of a list and squares it, if it is an integer.
```python
listToSquare = [1,2,3,'x',4]
squaredList = [x**2 for x in listToSquare if type(x) == types.IntType]
```
`x**2` is the output function, `listToSquare` is the input list, and `if type(x) == types.IntType` is the predicate that  
filters the original list.  
The same can be accomplished using `map` and `filter`.
```python
listToSquare = [1,2,3,'x',4]
squaredList = map(lambda x: x**2, filter(lambda x: type(x) == types.IntType, listToSquare)
```
These both produce the same result, however, the list comprehension method is preferred due to efficiency. This is because  
the `map` and `filter` version has two separate calls to define functions with lambda, which is a costly operation in Python.  
  
> List comprehensions can also be used on sets and dictionaries. The only difference between a set and list comprehension is that  
a set is returned.  
Here's an example that takes a list of strings and returns a set of the same strings, but capitalized.
```python
strings = ['abc','def','ghi']
stringsUpper = {s.upper() for s in strings}
```
  
> Dictionary comprehensions are much the same, in that they return a dictionary. Here's a comprehension that takes a list of  
integers and creates a dictionary where the key is the original integer and the value is that integer squared.
```python
keys = [1,2,3,4]
dict = {k: k**2 for k in keys}
```

-----------------------------------------------------------------------------------

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





