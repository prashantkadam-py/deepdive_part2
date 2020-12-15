# Context Manager

- It implements following protocol : 
   - \_\_enter\_\_ :
        - This method should perform whatever setup it needs to.
        - It can optionally return an object.
   
   - \_\_exit\_\_ : 
        - Runs even if an exception occurs in with block like try-finally.
        
- Common Patterns :
    - open-close
    - lock-release
    - change-reset
    - start-stop
    - enter-exit
   
- with ContextManager() as ctx:
    - creates instance of ContextManager class.
    - calls its \_\_enter\_\_ method.
    - return value from \_\_enter\_\_ is assigned to ctx.
    - after the with block, or if an exception occurs inside the with block its \_\_exit\_\_ method is called.
    
    
      