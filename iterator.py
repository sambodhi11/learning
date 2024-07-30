
t= ("a","b","c")
i=iter(t)
print(next(i))
print(next(i))
print(next(i))


class M:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
obj= M()
c = iter(obj)

for x in c:
  print(x)