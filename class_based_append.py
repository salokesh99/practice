

class MovingTotal:

    def __init__(self, numbers=[]) -> None:
        self.numbers = numbers
        

    def append(self, numbers):
        """
        :param numbers: (list) The list of numbers.
        """
        # print('numbers', numbers)
        # print('self.numbers', self.numbers)
        if len(self.numbers) == 0 :
            self.numbers = numbers
        else:
            for i in numbers :
                self.numbers.append(i)
        print('numbers after update --- > ')
        print('numbers', numbers)
        print('self.numbers', self.numbers)

        
        
    def contains(self, total):
        """
        :param total: (int) The total to check for.
        :returns: (bool) If MovingTotal contains the total.
        """
        numbers = self.numbers
        # if total in numbers :
        #     print("it is present---", self.numbers, numbers)

        found = False 

        for i in range(0, len(numbers)):
            # if (i+2) < len(numbers) and (i+3)<=len(numbers):
            if (i+3)<=len(numbers):
                t = sum(numbers[i:(i+3)])
                if t == total :
                    print('sum array slice - --- > ', f'numbers[{i}:{(i+3)}]',  numbers[i:(i+3)])
                    found = True
                    return True
        
        if not found :
            return False

                

    
if __name__ == "__main__":
    movingtotal = MovingTotal()
    
    movingtotal.append([1, 2, 3, 4])
    print(movingtotal.contains(6))
    print(movingtotal.contains(3))
    print(movingtotal.contains(12))
    print(movingtotal.contains(7))
    
    movingtotal.append([5])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    print(movingtotal.contains(7))