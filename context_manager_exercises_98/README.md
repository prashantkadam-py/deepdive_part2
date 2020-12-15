# Context Manager

- It implements following protocol : 
   - \_\_enter\_\_ :
        - This method should perform whatever setup it needs to.
        - It can optionally return an object.
   
   - \_\_exit\_\_ : 
        - Runs even if an exception occurs in with block like try-finally.
        - input for method exc_type, exc_value, exc_trace.
        - It returns True / False :
            - True : Silence any raised exception.
            - False : do not silence a raised exception.
        
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
    
 
 ## context_manager_classes_98.py 
 context manager basic examples.
 
 ## context_manager_use_cases_102.py
   - Precision (change decimal precision) 
   - Timer (calculate elapsed time)
   - OutToFile (change system out )
   
 ## context_manager_decorator_106.py
 - created custom context manager decorator from scratch.
 - use contextlib for inbuilt contextmanager.
      
