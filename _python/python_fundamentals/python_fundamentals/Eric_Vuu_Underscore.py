class Underscore:
    def map(self, iterable, callback):
        output = []
        for x in iterable:
          output.append(callback(x))
        return output

    def find(self, iterable, callback):
        for x in iterable:
          if callback(x) == True:
            return x

    def filter(self, iterable, callback):
        output = []
        for x in iterable:
          if callback(x) == True:
            output.append(x)
        return output

    def reject(self, iterable, callback):
        output = []
        for x in iterable:
          if callback(x) == False:
            output.append(x)
        return output



_ = Underscore()
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above

print(evens)

print(_.map([1,2,3], lambda x: x*2)) # should return [2,4,6]
print(_.find([1,2,3,4,5,6], lambda x: x>4)) # should return the first value that is greater than 4
print(_.filter([1,2,3,4,5,6], lambda x: x%2==0)) # should return [2,4,6]
print(_.reject([1,2,3,4,5,6], lambda x: x%2==0)) # should return [1,3,5]
