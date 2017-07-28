'''
From 
https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=2144
https://uva.onlinejudge.org/external/112/11203.pdf

 0 => no init yet
 1 => X
 2 => M
 3 => Y
 4 => E
 5 => Z
 6 => End ok
 7 => error

xM?Ex? where x > 0
for xMyEz where x,y,z > 0
xMy?Ez?
'''
def parse(strToChek):
  state = 0
  x = 0
  y = 0
  z = 0
  
  for c in strToChek:
    # state 0 not init
    if state == 0:
      if c == '?':
        state = 1
        x += 1
        continue
      return False
    # state 1 X
    if state == 1:
      if c == '?':
        x += 1
        continue
      if c == 'M':
        state = 2
        continue
      return False
    # state 2 M
    if state == 2:
      if c == '?':
        state = 3
        y += 1
        continue
      return False
    # state 3 Y
    if state == 3:
      if c == '?':
        y += 1
        continue
      if c == 'E':
        state = 4
        continue
      return False
    # state 4 E
    if state == 4:
      if c == '?':
        state = 5
        z += 1
        continue
      return False
    # state 5 Z
    if state == 5:
      if c == '?':
        z += 1
        continue
      return False
  
  if state == 5:
    return (x,y,z)
  return False
  
#xM?Ex? where x > 0
def isAxiom(x,y,z):
  return x > 0 and y > 0 and z == x+1

#for xMyEz where x,y,z > 0
#xMy?Ez?  
def isTheoreme(x,y,z):
  if isAxiom(x,y,z):
    return True
  if x == 0 or y == 0 or z == 0:
    return False
  return isTheoreme(x,y-1,z-1)



n = int(input())

for i in range(0,n):
  testStr = input()
  parsed = parse(testStr)
  if parsed == False:
    print("no-theorem")
    continue
  (x,y,z) = parsed
  if isTheoreme(x,y,z):
    print("theorem")
  else:
    print("no-theorem")
  
