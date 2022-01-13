from time import sleep
from threading import Lock
from threading import Thread

class MeuThread(Thread):
    def __init__(self, tempo, texto):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)

t1 = MeuThread('Thread 1', 5)
t1.start()

t2 = MeuThread('Thread 2', 3)
t2.start()

t3 = MeuThread('Thread 3', 2)
t3.start()
#
# for i in range(20):
#     print(i)
#     sleep(1)