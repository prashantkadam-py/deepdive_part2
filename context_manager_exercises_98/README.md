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
