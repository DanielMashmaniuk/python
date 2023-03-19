sandvich_orders = ['potato_sandvich','cocumber_sandvich','fish_sandvich','pastrami','pastrami','pastrami']
finished_sandviches = []

print('У нвс закінчилася пастрома')

while 'pastrami' in sandvich_orders  :
    sandvich_orders.remove('pastrami')
    
while sandvich_orders:
    
   sandvich_order = sandvich_orders.pop()
   print(f' Я приготував вам :{sandvich_order}')
   
   finished_sandviches.append(sandvich_order)
   
print(finished_sandviches)
   