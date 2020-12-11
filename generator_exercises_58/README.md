# Generators

## Generator Terminology, Working and States :
  
  ### Example :
    
    def my_func():
      print("Hello")
      yield "World"         __STATE__ : SUSPENDED
      return "Bye"          __STATE__ : CLOSED (ex. list(gen))
    
    gen = my_func()         __STATE__ : CREATED
    
    - my_fucn() : generator factory
    - gen : generator object 
    - next(gen) :           __STATE__ : RUNNING
          - Executes generator until "yield" statement and then it suspend itself, until next yield is called again.
          - If it encounters "return" before "yield" StopIteration exception occurs.
          - Calling next on the function resumes running the function right after the yield statement.
      
## factorial_generator_59.py
Implement Factorial using generator and math module.

## fibonacci_generator_60.py
Implement Fibonacci series using generator.

## iterable_generator_62.py
Implement SquaresIterable using squares generator.

## card_deck_generator_63.py
Implement Card Deck Example with reversed functionality using generator.

## yield_from_67.py
Example of yield from.
          
    
    
  
