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
