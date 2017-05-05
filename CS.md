### Actor Model

When you start talking about concurrency, you are trying to solve resource problems. Concurrency with threads and locks are pretty easy to do wrong. The actor model helps to force you to program concurrent portions of your code as self contained nuggets that can be performed in parallel and without depending on another piece of code. You are trying to avoid nastiness like race conditions and deadlocks.

Actors are like you and I in this conversation. You just can't reach into my brain and pick out what I'm typing. You passed me a message saying "Why do we exist?" I sat and crunched some numbers and sent a reply "I think, therefore I am." You couldn't tell what I was doing on my own slice of planet Earth the only contact you have with me is through the messages we pass back and forth.




### Flyweight Pattern



### Heavy Light Decomposition

HLD of a rooted tree is a method of decomposing the vertices of the tree into disjoint chains (no two chains share a node), to achieve important asymptotic time bounds for certain problems involving trees.


### Stack vs Heap

Stack is used for static memory allocation and Heap for dynamic memory allocation, both stored in the computer's RAM .

Variables allocated on the stack are stored directly to the memory and access to this memory is very fast, and it's allocation is dealt with when the program is compiled. When a function or a method calls another function which in turns calls another function etc., the execution of all those functions remains suspended until the very last function returns its value. The stack is always reserved in a LIFO(Last in first out) order, the most recently reserved block is always the next block to be freed. This makes it really simple to keep track of the stack, freeing a block from the stack is nothing more than adjusting one pointer.

Variables allocated on the heap have their memory allocated at run time and accessing this memory is a bit slower, but the heap size is only limited by the size of virtual memory . Element of the heap have no dependencies with each other and can always be accessed randomly at any time. You can allocate a block at any time and free it at any time. This makes it much more complex to keep track of which parts of the heap are allocated or free at any given time.

You can use the stack if you know exactly how much data you need to allocate before compile time and it is not too big.You can use heap if you don't know exactly how much data you will need at run-time or if you need to allocate a lot of data.

In a multi-threaded situation each thread will have its own completely independent stack but they will share the heap. Stack is thread specific and Heap is application specific. The stack is important to consider in exception handling and thread executions.

### Tail Recursion

Tail recursion is a special kind of recursion where the recursive call is the very last thing in the function. It's a function that does not do anything at all after recursing.

This is important because it means that you can just pass the result of the recursive call through directly instead of waiting for it—you don't have to consume any stack space. A normal function, on the other hand, has to have a stack frame so that the compiler knows to come back to it (and have all the necessary variable values) after the recursive call is finished.

Some languages recognize this and implement "proper tail calls" or "tail call elimination": if they see a recursive call in tail position, they actually compile it into a jump that reuses the current stack frame instead of calling the function normally. This improves the memory usage of the function asymptotically and prevents it from overflowing the stack. With this behavior, tail recursion is actually generally a good thing: chances are you do want to write your functions in a tail-recursive form if you can.

Certain languages like Scheme promise proper tail calls in the standard, so you can always rely on them. In other languages like OCaml, the compiler gives you the same promise even if there is no formal language standard.

Tail recursion only starts being a problem in languages which do not promise to implement them properly. Some compilers, like GCC, offer it as an optimization. However, it isn't guaranteed, and you never want to rely on an optimization to make your code correct! (Remember: without proper tail calls, you could easily run out of stack space.) Other languages like Python don't even offer it as an optimization.

In these cases, you can always rewrite your tail recursive function as a loop—which are, presumably, guaranteed to run in constant space. Better yet, you can always switch to a language that *does* support proper tail calls ;).
