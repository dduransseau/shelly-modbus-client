

from src import ShellyProModbusClient


def read_shellypro_metrics(address):
    client = ShellyProModbusClient(address)
    print(client.model)
    for m in client.get_energy_meter(index=0):
        print(m)
    for m in client.get_energy_meter(index=1):
        print(m)
    for m in client.get_energy_data(index=0):
        print(m)
    for m in client.get_energy_data(index=1):
        print(m)

if __name__ == "__main__":
    read_shellypro_metrics('<ip_address>')