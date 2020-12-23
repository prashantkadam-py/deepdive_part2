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
      
