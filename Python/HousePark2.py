class House6:
	lastname = "육"
	def __init__(self, name):
	    self.fullname = self.lastname + name
	def travel(self, where):
		print "%s, %s여행을 가 다 ." % (self.fullname, where) 
	def love(self, other):
		print "%s, %s 사 랑에 빠졌네" % (self.fullname, other.fullname) 
	def fight(self, other):
		print "%s, %s 싸우네" % (self.fullname, other.fullname) 
	def __add__(self, other):
		print "%s, %s 결혼했 네" % (self.fullname, other.fullname) 
	def __sub__(self, other):
		print "%s, %s 이 혼했 네" % (self.fullname, other.fullname) 
	def __del__(self):
		print "%s 죽네" % self.fullname

class HouseJung(HousePark):
	lastname = "정"
	def travel(self, where, day):
		print "%s, %s여행 %d일 가네" % (self.fullname, where, day)
