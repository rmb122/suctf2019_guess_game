pickle 本质是个栈语言, 不同于 json 亦或是 php 的 serialize. 实际上是运行 pickle 得到的结果是被序列化的对象.  
所以只要构造出 pickle 代码获得 guess_game.game, 然后修改 game 的 win_count 和 round_count 即可,  
注意这里必须手写, 如果是 `from guess_game import game`, 然后修改再 dumps 这个 game 的话, 是在运行时重新新建一个 Game 对象,
而不是从 guess_game 这个 module 里面获取.

然后注意

```python
ticket = restricted_loads(ticket)

assert type(ticket) == Ticket
```

所以还需要栈顶为一个 Ticket, 这比较方便, 可以 dumps 一个 Ticket 拼到之前手写的后面就可以了.

ref: https://www.leavesongs.com/PENETRATION/code-breaking-2018-python-sandbox.html  
