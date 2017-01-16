


#### Tail Recursion

Tail recursion is a special kind of recursion where the recursive call is the very last thing in the function. It's a function that does not do anything at all after recursing.

This is important because it means that you can just pass the result of the recursive call through directly instead of waiting for it—you don't have to consume any stack space. A normal function, on the other hand, has to have a stack frame so that the compiler knows to come back to it (and have all the necessary variable values) after the recursive call is finished.

Some languages recognize this and implement "proper tail calls" or "tail call elimination": if they see a recursive call in tail position, they actually compile it into a jump that reuses the current stack frame instead of calling the function normally. This improves the memory usage of the function asymptotically and prevents it from overflowing the stack. With this behavior, tail recursion is actually generally a good thing: chances are you do want to write your functions in a tail-recursive form if you can.

Certain languages like Scheme promise proper tail calls in the standard, so you can always rely on them. In other languages like OCaml, the compiler gives you the same promise even if there is no formal language standard.

Tail recursion only starts being a problem in languages which do not promise to implement them properly. Some compilers, like GCC, offer it as an optimization. However, it isn't guaranteed, and you never want to rely on an optimization to make your code correct! (Remember: without proper tail calls, you could easily run out of stack space.) Other languages like Python don't even offer it as an optimization.

In these cases, you can always rewrite your tail recursive function as a loop—which are, presumably, guaranteed to run in constant space. Better yet, you can always switch to a language that *does* support proper tail calls ;).
