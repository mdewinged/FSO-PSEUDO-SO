# Brief: Define the usage of the resources
# Author: Alexandre Kaihara and Pedro

from threading import Semaphore
from types import prepare_class

'''
1.3 Estrutura dos Recursos Disponíveis
O pseudo-SO deve, além de escalonar o processo no compartilhamento da CPU, e gerenciar o
espaço de memória de acordo com as áreas reservadas, ele deve gerenciar os seguintes recursos:
• 1 scanner
• 2 impressoras
• 1 modem
• 2 dispositivos SATA
Todos os processos, com exceção daqueles de tempo-real podem obter qualquer um desses
recursos. O pseudo-SO deve garantir que cada recurso seja alocado para um proceso por vez. Portanto, não
há preempção na alocação dos dispositivos de E/S. Assim, processos de tempo-real não precisam de
recursos de I/O.
'''

class ResourceManager():
    # Brief: 
    #   Init all structures to control the access to I/O devices
    #   OBS: All shared variables between all methods must use locks
    # Param:
    #   processID: Process identification
    # Return: 
    #   None
    def __init__(self) -> None:
        self.__ready_processes_buffer = []
        self.scanner = Semaphore(1)
        self.printer1  = Semaphore(2)
        self.modem   = Semaphore(1)
        self.sata    = Semaphore(2)

    # Brief: 
    #   Insert a blocked process on buffer to be reinserted on the queue
    # Param:
    #   processID: Process identification
    #   priority: Priority of the process
    # Return: 
    #   None
    def insert_buffer(self, processID: int, priority: int) -> None:
        self.__ready_processes_buffer.append((processID, priority))

    # Brief: 
    #   Get all buffered process id
    # Param:
    # Return: 
    #   None
    def get_buffer(self) -> None:
        return self.__ready_processes_buffer

    # Brief: 
    #   Empty buffer
    # Param:
    # Return: 
    def empty_buffer(self) -> None:
        self.__ready_processes_buffer = []

    # Brief: 
    #   Try to get the access to the scanner, if not, block the process till is free to use
    # Param:
    #   processID: Process identification
    # Return: 
    #   None
    def get_scanner(self, processID: int, priority: int) -> None:
        '''Implementar'''
        self.insert_buffer(processID, priority)

    # Brief: 
    #   Try to get the access to the printer, if not, block the process till is free to use
    # Param:
    #   processID: Process identification
    # Return: 
    #   None
    def get_printer(self, processID: int, priority: int) -> None:
        '''Implementar'''
        self.insert_buffer(processID, priority)
    
    # Brief: 
    #   Try to get the access to the modem, if not, block the process till is free to use
    # Param:
    #   processID: Process identification
    # Return: 
    #   None
    def get_modem(self, processID: int, priority: int) -> None:
        '''Implementar'''
        self.insert_buffer(processID, priority)
    
    # Brief: 
    #   Try to get the access to the sata, if not, block the process till is free to use
    # Param:
    #   processID: Process identification
    # Return: 
    #   None
    def get_sata(self, processID: int, priority: int) -> None:
        '''Implementar'''
        self.insert_buffer(processID, priority)
    