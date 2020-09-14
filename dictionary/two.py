a = [10, 20, 30, 40]

print(type(a),a) # type: list - [10, 20, 30, 40]

b=list(reversed(a))
print(b) # [40, 30, 20, 10]

c=set(reversed(a))
d=tuple(reversed(a))
print(type(c),c) # type set - {40, 10, 20, 30}
print(type(d),d) # type tuple - (40, 30, 20, 10)


