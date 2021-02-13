ip_str = 'Halo nama saya sopan setiawan, saya sedang belajar python'

ip_str = ip_str.casefold()

count = {X:sum([1 for char in ip_str if char == X]) for X in 'aiueo'}

print(count)