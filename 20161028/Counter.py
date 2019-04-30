from collections import Counter
basket=['apple','orange','apple','pear','orange','banana']
Counter(basket)
Counter({'orange': 2, 'apple': 2, 'banana': 1, 'pear': 1})
c=Counter(basket)
c.most_common()
[('orange', 2), ('apple', 2), ('banana', 1), ('pear', 1)]
c.most_common(2)
[('orange', 2), ('apple', 2)]