# nqueens

1.- Download the project using the following command: 
        git clone https://github.com/fbanquez/nqueens.git

2.- Once downloaded the application build the containers with the instruction:
        docker-compose build

3.- After the construction is finished, start the execution of the containers 
    with the command:
        docker-compose up

4.- The application with N = 8 will be executed automatically 1 minute after 
    the previous step.

5.- You can check the results of the run by entering the database with the 
    following instructions:
        docker exec -it nqueens_nqueens_1 /bin/sh
        psql -U postgres -d nqueens  (password: postgres)
        select * from solutions;
    You will see a record for each solution for the given N.

6.-Because it's a script, after the execution the container stops, so it must 
   be restarted to run it again with the following instruction:
        docker-compose restart

7.- If you want to change the value of N you must first start the container with 
    the instruction:
        docker start -ia nqueens_nqueens_1
    and then edit the 'app.py' file, placing a new brand in order to easily 
    identify it in the database. After this, perform the previous step to restart 
    the run.
