""" 
    * Agendamento de Desligamento PC
    -> Crie duas funcoes em python para agendar o desligamento do computador em uma hora e meia hora.
"""

# 1 - Desligar o computador
#os.system('shutdown /s') # Desliga o computador em 60s
# os.system('shutdown /s /t 0') # Desliga o computador imediatamente

# 2 - Cancelar desligamento
# os.system('shutdown /a')
import os

def turn_off_one_hour():
    os.system('shutdown /s /t 3600')
    
def turn_off_half_an_hour():
    os.system('shutdown /s /t 1800')
    
def cancel_shutdown():
    os.system('shutdown /a')

# turn_off_one_hour()
cancel_shutdown()
# turn_off_one_hour()