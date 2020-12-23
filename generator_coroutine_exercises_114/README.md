# Generator as Coroutine 

## Concurrency vs Parallelism
 - Concurrency :
    __task1__ --> __task2__ --> __task1__ --> __task2__
    
 - Parallelism :
    __task1__ --> -->
    __task2__ --> -->

## Cooperative vs Preemptive Multitasking
  - Cooperative :
    __task1__ --> voluntary yield --> __task2__ --> voluntary yield
    
    Completely controlled by developer.
   
  - Preemptive :
    __task1__ --> not voluntary -->   __task2__ --> not voluntary
  
    Not controlled by developer some sort of scheduler involved.
    
  __Note__ : 
          Python threading is inbetween cooperative and preemptive. 
        
## Coroutines : 
  - Cooperative multitasking 
  - concurrent not parallel.
  - Python program executes on a single thread (GIL).
  - Two ways to create coroutines in Python : 
      - generators uses extended yield
      - asyncio native corutines uses async/await.
      
## Generator close : 
   - Python's expectations when close() is called :
      - __GeneratorExit__ exception bubbles up
      - The generator exits cleanly (returns).
      - The exception is silenced by python.
      - To the caller everything works normally.
      - If generator ignores the GeneratorExit exception and yields another value. Python raises a RuntimeError : generator ignored GeneratorExit.
      __Note__ : Don't try to catch and ignore a GeneratorExit exception. It's perfectly OK not to catch it, and simply let it bubble up.
  
## Sending things to coroutines :
      - send(data) : sends data to coroutine.
      - close() : sends(throws) a GeneratorExit exception to coroutine.
      - throw(exception, value) : We can send any exception to coroutine.
      - the exception is raised at the point where the coroutine is SUSPENDED.
      
## gen.throw(exception, value) :
   
   ### TYPE I : 
        Generator does not catch the exception (does nothing). Exception propogates back to the caller.
      
   ### TYPE II :
        - catch and yield : 
           - generator catches the exception.
           - handles and silences the exception.
           - yields a value.
           - generator is now SUSPENDED.
           - yielded value is the return value of the throw() method.
        
        - catch and return : 
           - generator catches the exception.
           - generator exits (returns).
           - caller receives a StopIteration exception.
           - generator is now CLOSED.
           - this is same as calling send() or next() to generator that returns instead of yielding.
           - can think of throw() as same thing as send(), but causes an exception to be sent instead of plain data.
          
        - catch and raise different exception : 
           - generator catches the exception.
           - generator handles exception and raises another exception.
           - new exception propogates to the caller. 
           - generator is now CLOSED. 
