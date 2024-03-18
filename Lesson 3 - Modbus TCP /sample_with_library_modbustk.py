import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp

SERVER_IP = "10.53.36.249"
SERVER_PORT = 502
UNIT_ID = 1
# Первый адрес для опроса
START_REGS = 1
# Кол-во регистров после первого
NUM_REGISTERS = 10


def read_holding_regs(ip, port, address, start_register, num_registers):
    try:
        master = modbus_tcp.TcpMaster(ip, port, timeout_in_sec=1)
        return master.execute(address, cst.READ_INPUT_REGISTERS, start_register, num_registers)
    except BaseException as err:
        return err

if __name__ == "__main__":
    print(read_holding_regs(SERVER_IP, SERVER_PORT, UNIT_ID, START_REGS, NUM_REGISTERS))
