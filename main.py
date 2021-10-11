import time
from threading import Thread, Lock
import threading

tenedores_disponilbes = 2

def comer(mutex):
    global tenedores_disponilbes
    name_hilo = threading.current_thread().getName()
    print(f'Filosofo {name_hilo} se sienta')
    time.sleep(2)
    mutex.acquire()
    if(tenedores_disponilbes == 2):
        print(f'Filosofo {name_hilo} tiene 2 tenedores')
        tenedores_disponilbes = 0
        time.sleep(2)
        print(f'Filosofo {name_hilo} esta comiendo')
        time.sleep(2)
        print(f'Filosofo {name_hilo} termino de comer')
        tenedores_disponilbes = 2
        time.sleep(2)
        print(f'Filosofo {name_hilo} esta lavando el tenedor')
        time.sleep(2)            
    mutex.release()
    
if __name__ == "__main__":
    mutex = Lock()
    filosofo_1 = Thread(name='1',target=comer, args=(mutex,))
    filosofo_2 = Thread(name='2',target=comer, args=(mutex,))
    filosofo_3 = Thread(name='3',target=comer, args=(mutex,))
    filosofo_4 = Thread(name='4',target=comer, args=(mutex,))
    filosofo_5 = Thread(name='5',target=comer, args=(mutex,))
    
    filosofo_1.start()
    filosofo_2.start()
    filosofo_3.start()
    filosofo_4.start()
    filosofo_5.start()

