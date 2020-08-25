Slicing用于从一个字符串中获取多个字符（一个子串）。它的语法类似于索引，但是使用两个索引（数字），用冒号隔开，例如`str[ind1:ind2]`。
##### 示例
<pre><code>
str[start:end] # 从start到end-1
str[start:] # 从数组的start开始的其余部分。
str[:end] # 从开始到end-1
str[:] # 整个数组的副本。
</code></pre>

使用slicing从`monty_python`变量中获取`"Python"`。 

<div class='hint'>可以将一个或两个索引留空。</div>
