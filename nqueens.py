# -*- coding: utf-8 -*-
"""
This module solves the N-Queens puzzle's problem that consists of placing N chess 
queens on a board of NxN size without being threatened each other.

Examples:
    If you use it as a package you must import it and use it in the following way:

    >> from nqueens import *
    >> x = 8
    >> app = NQueens(x)
    >> app.findAllSolutions()

    If you use it as a script, you should use it in the following way:

    $ python NQueens.py

"""

from array import *
from interface_db import *

class NQueens(object):
    """
    """

    def __init__(self, N=1, mark='Dummy'):
        """
        Class constructor.

        Args:
            N ('int', optional): indicates the chessboard's size and the number 
                                 of queens to place on it.

            mark ('string', optional): identification of the process' execution.

        """
        self.N = N
        self.count = 0
        self.solution = array('i')
        self.db = InterfaceDB(mark, N)
        
        if not self.db.connect('postgres', 'postgres', 'nqueens'):
            print('Problems establishing database connection')

        if not self.db.create_table():
            print("Problems creating database's table")

        for i in range(self.N):
            self.solution.append(-1)


    def showSolution(self):
        """
        """
        self.count += 1
        print('{0} - {1}'.format(self.count, self.solution.tolist()))


    def diagonal(self, x, y):
        """
        This method is used to know if a queen is on the diagonal of another one.
        """
        return abs(x-y)


    def isValid(self, sol, col):
        """
        This method determines if the queen we are placing is attacked by the 
        queens placed previously.

        Args:
            sol ('array'): array of N positions that stores the indices of the 
                           rows where we placed the queens.

            col ('int'): current column where we are placing the new queen.

        Returns:
            (boolean): True when we fix the queen in the current row, False otherwise.

        """
        #  Test each of the queens that were previously placed
        for i in range(col):
            # Evaluate if the current queen share row or diagonal with another piece.
            # The column is not evaluated because we only place one piece per column
            if(sol[i] == sol[col] or
               self.diagonal(sol[i], sol[col]) == self.diagonal(i, col)):
                return False

        return True


    def findAllSolutions(self, column=0):
        """
        Method is responsible for finding all possible solutions to the problem of 
        N-Queens, this code implements Backtracking to find the array with the 
        results.

        Args:
            column ('int', optional): represents the index of the column where 
                         the queen will be placed.

        Returns:
            A boolean value.

        """
        if(column >= self.N):
            #self.showSolution()
            self.db.insert_solution(self.solution.tolist())
            return True

        # Initializing variables
        hit = False
        self.solution[column] = -1

#        import pdb; pdb.set_trace()
        while True:
            # Indicates the index of the row where the queen will be evaluated
            self.solution[column] += 1

            # It is evaluated if the queen can be in the row of the current column
            if(self.isValid(self.solution, column)):
                if(column < self.N):
                    # After the queen has been placed in its cell, restart the 
                    # process for the next column
                    hit = self.findAllSolutions(column + 1)
                if(self.solution[column] < (self.N - 1)):
                    hit = False
            # Exit loop if you reach the last row of the column or when a solution 
            # has been found
            if((self.solution[column] >=  (self.N - 1)) or hit):
                break

        return hit


    def terminate(self):
        self.db.close()

