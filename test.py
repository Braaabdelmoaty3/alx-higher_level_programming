items =[("product1", 9),
        ("product2", 5),        
        ("product3", 99),
]
def sortItem(item):
    return item[1]


items.sort(key=sortItem)
print(items)