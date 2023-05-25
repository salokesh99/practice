from threading import Thread
from time import sleep

# done = False

# def counts():
#     i=0
#     while not done:
#         sleep(1)
#         print(i)
#         i +=1



# Thread(target=counts, daemon=True).start()
# input('press enter to stop!!!')
# done = True

#daemon ends a thread, when execution is over
# done = False

# def counts():
#     i=0
#     while True:
#         sleep(1)
#         print(i)
#         i +=1



# Thread(target=counts, daemon=True).start()
# input('press enter to stop!!!')
# done = True

# done = False

# def counts(text):
#     i=0
#     while not done:
#         sleep(1)
#         print(f'{text} - {i}')
#         i +=1



# Thread(target=counts, daemon=True, args=('raam',)).start() 
# Thread(target=counts, daemon=True, args=('Jai Shree ',)).start() 


# input('press enter to stop!!!')
# done = True

# run infinitely
# done = False

# def counts(text):
#     i=0
#     while True:
#         sleep(1)
#         print(f'{text} - {i}')
#         i +=1



# Thread(target=counts, daemon=True, args=('raam',)).start() 
# Thread(target=counts, daemon=False, args=('Jai Shree ',)).start() 


# input('press enter to stop!!!')
# done = True

# done = False

# def counts(text):
#     i=0
#     while True:
#         sleep(1)
#         print(f'{text} - {i}')
#         i +=1



# Thread(target=counts, daemon=False, args=('raam',)).start() 
# Thread(target=counts, daemon=False, args=('Jai Shree ',)).start() 


# input('press enter to stop!!!')
# done = True

# done = False

# def counts(text):
#     i=0
#     while True:
#         sleep(1)
#         print(f'{text} - {i}')
#         i +=1



# Thread(target=counts, daemon=True, args=('raam',)).start() 
# Thread(target=counts, daemon=True, args=('Jai Shree ',)).start() 


# input('press enter to stop!!!')
# done = True

# done = False

# def counts(text):
#     i=0
#     while True:
#         # sleep(1)
#         print(f'{text} - {i}')
#         i +=1



# t1 = Thread(target=counts, daemon=True, args=('raam',))
# t2 = Thread(target=counts, daemon=True, args=('Jai Shree ',))
# t1.start() 
# t2.start() 

# input('press enter to stop!!!')
# done = True


done = False

def counts(text):
    i=0
    while True:
        sleep(1)
        print(f'{text} - {i}')
        i +=1



t1 = Thread(target=counts, daemon=True, args=('raam',))
t2 = Thread(target=counts, daemon=True, args=('Jai Shree ',))
t1.start() 
t2.start() 
t1.join()
t2.join()

input('press enter to stop!!!')
done = True