from collections import deque

class LRUCache:

	def __init__(self, capacity: int):
		self.size = capacity
		self.cache = dict()
		self.lru = deque()

	def get(self, key: int) -> int:
		if key in self.cache:
			self.lru.pop()
			self.lru.appendleft(key)
			return self.cache[key]
		return -1

	def put(self, key: int, value: int) -> None:
		if len(self.lru) < self.size:
			self.lru.appendleft(key)
			self.cache[key] = value
			return

		if len(self.cache.keys()) == self.size:
			if key in self.cache and self.lru[-1] == key:
				self.lru.pop()
				self.cache.pop(key)
			elif key not in self.cache:
				del_key = self.lru.pop()
				self.cache.pop(del_key)
			else:
				self.lru.remove(key)
				self.cache.pop(key)

			
			self.lru.appendleft(key)
			self.cache[key] = value
		
obj = LRUCache(2);
obj.put(1, 1)  # cache is {1=1}
obj.put(2, 2)  # cache is {1=1, 2=2}
# obj.put(2, 2)

print(obj.get(1))     # return 1
obj.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(obj.get(2))     # returns -1 (not found)
obj.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(obj.get(1))     # return -1 (not found)
print(obj.get(3))     # return 3
print(obj.get(4))     # return 4


from collections import OrderedDict
class LRUCache2:

	def __init__(self, capacity):
		self.cap = capacity
		self.cache = OrderedDict()

	def get(self, key):
		if key in self.cache:
			self.cache.move_to_end(key, False)
			return self.cache[key]
		return -1

	def put (self, key, value):
		if len(self.cache.items()) < self.cap:
			self.cache[key] = value
			return
		if len(self.cache.items()) == self.cap:
			if key not in self.cache:
				self.cache.popitem()
			self.cache[key] = value
			self.cache.move_to_end(key, False)


obj = LRUCache2(2);
obj.put(1, 1)  # cache is {1=1}
obj.put(2, 2)  # cache is {1=1, 2=2}
obj.put(2, 2)  # should make it MRU

print(obj.get(1))     # return 1
obj.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(obj.get(2))     # returns -1 (not found)
obj.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(obj.get(1))     # return -1 (not found)
print(obj.get(3))     # return 3
print(obj.get(4))     # return 4



