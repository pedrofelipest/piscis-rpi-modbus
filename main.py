from pymodbus.client.sync import ModbusTcpClient
from time import sleep

HOST = '10.106.23.17'
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
E_ATIVA = 49184
E_REATIVA = 49192
I_MEDIA_ABC = 49200
FATOR_POTENCIA = 49208


client = ModbusTcpClient(host=HOST, port=PORT)

def resetPort(port):
    global client

    for i in range(3):
        client.write_coils(port,1)

    client.write_coils(port,1)
    sleep(3)
    client.write_coils(port,0)


def ReadHoldingRegister(address, bytes=1):
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
        r = client.read_discrete_inputs(address, bits)
        data = r.bits[0]
    
    return data

resetPort(RS485)

resetPort(ORP)
orp = ReadHoldingRegister(8005)

resetPort(CONDUTIVIDADE)
condutividade = ReadHoldingRegister(8002)

resetPort(TURBIDEZ)
turbidez = ReadHoldingRegister(8004)

resetPort(PH)
ph = ReadHoldingRegister(8001)

resetPort(OD)
od = ReadHoldingRegister(8003)

resetPort(TEMPERATURA)
temperatura = ReadHoldingRegister(8010)

alimentador = ReadCoils(16004)
aerador = ReadCoils(16001)
filtro = ReadCoils(16000)
emergencia = ReadDiscreteInputs(16000)

resetPort(T_AB)
t_ab = ReadHoldingRegister(8020)

resetPort(T_BC)
t_bc = ReadHoldingRegister(8052)

resetPort(T_AC)
t_ac = ReadHoldingRegister(8024)

resetPort(E_ATIVA)
e_ativa = ReadHoldingRegister(8026)

resetPort(E_REATIVA)
e_reativa = ReadHoldingRegister(8028)

resetPort(I_MEDIA_ABC)
i_media_abc = ReadHoldingRegister(8030)

resetPort(FATOR_POTENCIA)
fator_potencia = ReadHoldingRegister(8032)

res = {'orp':orp,
       'condutividade':condutividade,
       'turbidez':turbidez,
       'ph':ph,
       'od':od,
       'temperatura':temperatura,
       'alimentador':alimentador,
       'aerador':aerador,
       'filtro':filtro,
       'emergencia':emergencia,
       't_ab':t_ab,
       't_bc':t_bc,
       't_ac':t_ac,
       'e_ativa':e_ativa,
       'e_reativa':e_reativa,
       'i_media_abc':i_media_abc,
       'fator_potencia':fator_potencia
       }

print(res)