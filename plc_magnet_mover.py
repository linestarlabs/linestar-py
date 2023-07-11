import os
from dotenv import load_dotenv
from pycomm3 import LogixDriver

class PLCMagnetMover:
    def __init__(self, ip_address):
        self.ip_address = ip_address
        self.driver = None

    def connect(self):
        self.driver = LogixDriver(self.ip_address)
        self.driver.open()

    def wake(self):
        if self.driver:
            self.driver.write("PowerOn", 1)
        else:
            raise Exception("Not connected to the PLC.")

    def move_to_home(self):
        if self.driver:
            self.driver.write("MoveToHome", 1)
        else:
            raise Exception("Not connected to the PLC.")

    def go_to_position(self, x, y):
        if self.driver:
            self.driver.write("GoToXPosition", x)
            self.driver.write("GoToYPosition", y)
        else:
            raise Exception("Not connected to the PLC.")

    def report_location(self):
        if self.driver:
            x = self.driver.read("CurrentXPosition")
            y = self.driver.read("CurrentYPosition")
            return f"({x} , {y})"
        else:
            raise Exception("Not connected to the PLC.")

    def report_error_margin(self):
        if self.driver:
            x_error = self.driver.read("XErrorMargin")
            y_error = self.driver.read("YErrorMargin")
            return f"({x_error} , {y_error})"
        else:
            raise Exception("Not connected to the PLC.")

    def close(self):
        if self.driver:
            self.driver.close()


if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()

    # Get the IP address from the environment variable
    ip_address = os.getenv("ETHERNET_IP_ADDRESS")

    # Example usage
    client = PLCMagnetMover(ip_address)
    client.connect()
    client.wake()
    client.move_to_home()
    client.go_to_position(4.5, 2.9)
    location = client.report_location()
    print(f"Current location: {location}")
    error_margin = client.report_error_margin()
    print(f"Error margin: {error_margin}")
    client.close()

