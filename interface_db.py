# -*- coding: utf-8 -*-
#
from sqlalchemy import (create_engine, insert, MetaData, Table, Column, String, 
                        Integer, DateTime)
from sqlalchemy.dialects import postgresql
from datetime import datetime


class InterfaceDB(object):
    
    def __init__(self, mark, n):
        """
        Class constructor.

        Args:
            n ('int', require): number os queens and size of boards.

            mark ('string', optional): identification of the process' execution.

        """
        self.mark = mark
        self.n = n
        self.engine = None
        self.connection = None
        self.metadata = MetaData()
        self.solutions = Table('solutions', self.metadata,
            Column('mark', String(50), nullable=False),
            Column('date', DateTime(), default=datetime.now),
            Column('n_value', Integer, nullable=False),
            Column('solution', postgresql.ARRAY(Integer), nullable=False)
        )


    def connect(self, user, passwd, db, host='pgdb', port=5432):
        """
        This method establishes the database's connection.
        """        
        try:        
            url = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(user, passwd, host, port, db)
            self.engine = create_engine(url, client_encoding='utf8')
            self.connection = self.engine.connect()
        except:
            return False
        
        return True


    def create_table(self):
        """
        This method creates the table where the solutions are stored.
        """
        # If the table doesn't exist.
        if not self.engine.dialect.has_table(self.engine, 'solutions'):
            # You cann't create a table if a connection isn't established
            if self.connection is not None:
                try:
                    self.solutions.create(self.connection)
                    return True
                except:
                    print('ERROR => create_table')
        else:
            return True
        
        return False


    def insert_solution(self, solution):
        """
        This method inserts a valid solution into the database.
        """
        # You cann't insert a solution if a connection isn't established
        if self.connection is not None:        
            try:
                # Building the insertion sentence
                insert = self.solutions.insert().values(
                            mark = self.mark,
                            n_value = self.n,
                            solution = solution
                         )
                # Executing the insertion statement
                self.connection.execute(insert)
                return True
            except:
                print('ERROR => insert_solution')

        return False


    def close(self):
        """
        Close the connection and release the engine
        """
        # the connection and the engine are set up
        if self.connection is not None or self.engine is not None:
            self.connection.close()
            self.engine.dispose()        

