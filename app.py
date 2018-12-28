from nqueens import *
import time

def main():
    app = NQueens(8, 'Matin')       # 'Matin' is a mark to identify the run.
    app.findAllSolutions()
    app.terminate()

if __name__ == '__main__':
    # This timeout is necessary when the docker-compose up command is executed
    time.sleep(60)       
    main()

