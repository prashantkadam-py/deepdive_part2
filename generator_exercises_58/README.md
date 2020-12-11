# Generators

## Generator Terminology and Working :
  
  ### Example :
    
    def my_func():
      print("Hello")
      yield "World"
    
    gen = my_func()
    
    - my_fucn() : generator factory
    - gen : generator object
    - next(gen) : 
          - executes generator until "yield" statement and then it suspend itself, until next yield is called again.
          - If it encounters "return" before "yield" StopIteration exception occurs.
          
    
    
  
