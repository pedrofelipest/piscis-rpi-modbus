from pymodbus.client.sync import ModbusTcpClient
from time import sleep
import requests

HOST = '192.168.0.52'

PORT = 502

RS485 = 49000
OD = 49008
TEMPERATURA = 49016
TURBIDEZ = 49024
ORP = 49032
CONDUTIVIDADE = 49040
PH = 49048
T_AB = 49160
T_BC = 49168
T_AC = 49176
#E_ATIVA = 49184
#E_REATIVA = 49192
#P_APARENTE = 49200
#I_MEDIA_ABC = 49200
#FATOR_POTENCIA = 49208


client = ModbusTcpClient(host=HOST, port=PORT)

def resetPort(port):
    global client

    client.write_coil(port,1)
    client.write_coil(port,1)
    sleep(.1)
    client.write_coil(port,1)
    client.write_coil(port,1)
    sleep(4)
    client.write_coil(port,0)
    client.write_coil(port,0)
    sleep(.1)
    client.write_coil(port,0)
    client.write_coil(port,0)

def ReadHoldingRegister(address, bytes=4):
    global client
    data = 0
    for i in range(2):
        r = client.read_holding_registers(address, bytes)
        data = r.registers[0]
    
    return data

def ReadDiscreteInputs(address, bytes=1):
    global client
    data = 0
    for i in range(2):
        r = client.read_discrete_inputs(address, bytes)
        data = r.bits[0]
    
    return data

def ReadCoils(address, bits=8):
    global client
    data = 0
    for i in range(2):
        r = client.read_coils(address, bits)
        data = r.bits[0]
   
    return data

resetPort(RS485)

resetPort(OD)
od = ReadHoldingRegister(8000)/100.00

resetPort(TURBIDEZ)
turbidez = ReadHoldingRegister(8004)/10.0

resetPort(ORP)
orp = ReadHoldingRegister(8006)

resetPort(CONDUTIVIDADE)
condutividade = ReadHoldingRegister(8008)*2000/65535.00

resetPort(PH)
ph = ReadHoldingRegister(8010)/100.00

resetPort(TEMPERATURA)
temperatura = ReadHoldingRegister(8002)/10.0

#aerador = ReadCoils(16000)
#filtro = ReadCoils(16001)
#alimentador = ReadCoils(16002)

#emergencia = ReadDiscreteInputs(16000)

resetPort(T_AB)
t_ab = ReadHoldingRegister(8020)*400.00/17678.5

resetPort(T_BC)
t_bc = ReadHoldingRegister(8022)*400.00/17763.4

resetPort(T_AC)
t_ac = ReadHoldingRegister(8024)*400.00/17817.2

#resetPort(E_ATIVA)
#e_ativa = ReadHoldingRegister(8026)

#resetPort(E_REATIVA)
#e_reativa = ReadHoldingRegister(8028)*400.00/32767.00

#resetPort(P_APARENTE)
#p_aparente = ReadHoldingRegister(8028)*400.00/32767.00

#resetPort(I_MEDIA_ABC)
#i_media_abc = ReadHoldingRegister(8030)*5/482272.75

#resetPort(FATOR_POTENCIA)
#fator_potencia = ReadHoldingRegister(8032)*400/6641336.117

res = {'orp':orp,
       'condutividade':condutividade,
       'turbidez':turbidez,
       'ph':ph,
       'od':od,
       'temperatura':temperatura,
       #'p_aparente':p_aparente,
       #'alimentador':alimentador,
       #'aerador':aerador,
       #'filtro':filtro,
       #'emergencia':emergencia,
       't_ab':t_ab,
       't_bc':t_bc,
       't_ac':t_ac
       #'e_ativa':e_ativa,
       #'e_reativa':e_reativa,
       #'i_media_abc':i_media_abc,
       #'fator_potencia':fator_potencia
       }
r  = requests.post('https://piscis-dev.herokuapp.com/data', json={"value":condutividade,"sensor":1, "location":1})
print(r.status_code)

r  = requests.post('https://piscis-dev.herokuapp.com/data', json={"value":ph,"sensor":3, "location":1})
print(r.status_code)

r  = requests.post('https://piscis-dev.herokuapp.com/data', json={"value":orp,"sensor":4, "location":1})
print(r.status_code)

r  = requests.post('https://piscis-dev.herokuapp.com/data', json={"value":od,"sensor":5, "location":1})
print(r.status_code)

r  = requests.post('https://piscis-dev.herokuapp.com/data', json={"value":round(t_ab,2),"sensor":10, "location":1})
print(r.status_code)

r  = requests.post('https://piscis-dev.herokuapp.com/data', json={"value":round(t_bc,1),"sensor":11, "location":1})
print(r.status_code)

r  = requests.post('https://piscis-dev.herokuapp.com/data', json={"value":round(t_ac,2),"sensor":12, "location":1})
print(r.status_code)

#r  = requests.post('https://piscis-dev.herokuapp.com/data', json={"value":e_ativa,"sensor":13, "location":1})
#print(r.status_code)

#r  = requests.post('https://piscis-dev.herokuapp.com/data', json={"value":p_aparente,"sensor":19, "location":1})
#print(r.status_code)

#r  = requests.post('https://piscis-dev.herokuapp.com/data', json={"value":i_media_abc,"sensor":15, "location":1})
#print(r.status_code)

#r  = requests.post('https://piscis-dev.herokuapp.com/data', json={"value":fator_potencia,"sensor":16, "location":1})
#print(r.status_code)

r  = requests.post('https://piscis-dev.herokuapp.com/data', json={"value":turbidez,"sensor":17, "location":1})
print(r.status_code)

r  = requests.post('https://piscis-dev.herokuapp.com/data', json={"value":temperatura,"sensor":18, "location":1})
print(r.status_code)

#r  = requests.post('https://piscis-dev.herokuapp.com/perifherals', json={"value":alimentador,"perifheral":1})
#print(r.status_code)

#r  = requests.post('https://piscis-dev.herokuapp.com/perifherals', json={"value":aerador,"perifheral":2})
#print(r.status_code)

#r  = requests.post('https://piscis-dev.herokuapp.com/perifherals', json={"value":filtro,"perifheral":3})
#print(r.status_code)

#r  = requests.post('https://piscis-dev.herokuapp.com/perifherals', json={"value":emergencia,"perifheral":4})
#print(r.status_code)

print(res)
