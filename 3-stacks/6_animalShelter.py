# Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first
# out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
# or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
# that type). They cannot select which specific animal they would like. Create the data structures to
# maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
# and dequeueCat. You may use the built-in Linkedlist data structure.


class Animal:
    def __init__(self, name, animalType, order=0):
        self.name = name
        self.animalType = animalType
        self.order = order

    def __repr__(self):
        return f"(Name: {self.name}, Type: {self.animalType}, Order: {self.order})"


class AnimalQueue:
    def __init__(self):
        self.catQueue = []
        self.dogQueue = []
        self.order = 0

    def enqueue(self, item: Animal):
        self.order += 1
        item.order = self.order
        if item.animalType == "Cat":
            self.catQueue.append(item)
        elif item.animalType == "Dog":
            self.dogQueue.append(item)

    def dequeueAny(self):
        if self.catQueue and self.dogQueue:
            if self.catQueue[-1].order > self.dogQueue[-1].order:
                return self.catQueue.pop(0)
            else:
                return self.dogQueue.pop(0)
        elif self.catQueue:
            return self.catQueue.pop(0)
        elif self.dogQueue:
            return self.dogQueue.pop(0)
        else:
            return None

    def dequeueDog(self):
        if not self.dogQueue:
            return None
        else:
            return self.dogQueue.pop(0)

    def dequeueCat(self):
        if not self.catQueue:
            return None
        else:
            return self.catQueue.pop(0)

    def print_queue(self):
        print(f"Cat: {self.catQueue}")
        print(f"Dog: {self.dogQueue}")


if __name__ == "__main__":
    queue = AnimalQueue()
    queue.enqueue(Animal("George", "Dog"))
    queue.enqueue(Animal("Jimmy", "Cat"))
    queue.enqueue(Animal("Henry", "Dog"))
    queue.enqueue(Animal("Jacky", "Dog"))
    queue.enqueue(Animal("Damien", "Cat"))
    queue.enqueue(Animal("Tom", "Dog"))
    # queue.print_queue()
    queue.dequeueAny()
    # queue.print_queue()
    queue.enqueue(Animal("Keith", "Dog"))
    # queue.print_queue()
    queue.dequeueDog()
    # queue.print_queue()
    queue.dequeueCat()
    # queue.print_queue()
