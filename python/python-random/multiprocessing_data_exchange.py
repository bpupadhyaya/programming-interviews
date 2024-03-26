from multiprocessing import Process, Pipe
from time import sleep


def my_worker(conn):
    print('Worker - sleeping for 1 second ')
    sleep(1)
    print('Worker - sending data via pipe ')
    conn.send('test data')
    print('Worker - closing worker end of connection')
    conn.close()


def main():
    print('Main - starting, creating the Pipe')
    main_connection, worker_connection = Pipe()
    p = Process(target=my_worker, args=[worker_connection])
    print('Main - starting the process')
    p.start()
    print('Main - wait for a response from the child process')
    print('Data received on main side: ', main_connection.recv())
    print('Main - closing parent process end of connection')
    main_connection.close()
    print('Main - done')


if __name__ == '__main__':
    main()
