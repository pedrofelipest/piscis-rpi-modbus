from pymodbus.client.sync import ModbusTcpClient

HOST = '192.168.0.147'

client = ModbusTcpClient(HOST)

def ReadHoldingRegister(address, bytes=1):
    global client
    data = 0
    for i in range(2):
        r = client.read_holding_registers(address, bytes)
        data = r.register[0]
    
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

orp = ReadHoldingRegister(8005)
condutividade = ReadHoldingRegister(8002)
turbidez = ReadHoldingRegister(8004)
ph = ReadHoldingRegister(8001)
od = ReadHoldingRegister(8003)
temperatura = ReadHoldingRegister(8010)
alimentador = ReadCoils(16004)
aerador = ReadCoils(16001)
filtro = ReadCoils(16000)
emergencia = ReadDiscreteInputs(16000)

res = {'orp':orp,
       'condutividade':condutividade,
       'turbidez':turbidez,
       'ph':ph,
       'od':od,
       'temperatura':temperatura,
       'alimentador':alimentador,
       'aerador':aerador,
       'filtro':filtro,
       'emergencia':emergencia}

print(res)