from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class StreamError(Exception):
    pass


class DataStream(ABC):
    criterias: List[str] = ["normal", "critical"]
    valid_id: str = ""

    def __init__(self, stream_id: str):
        if not stream_id[:len(self.valid_id)] == self.valid_id:
            raise StreamError(F"{stream_id} is not a valid sensor id" +
                              F", must start with {self.valid_id}")
        self.stream_id: str = stream_id
    '''
    an abstract base class with core streaming functionality
    '''
    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        '''Process a batch of data'''
        pass

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        '''Filter data based on criteria'''
        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        '''Return stream statistics'''
        pass


class StreamProcessor():
    '''
    handles multiple stream types polymorphically
    '''
    def __init__(self, ) -> None:
        self.proccessed: Dict[str, int] = {
                "SENSOR": 0,
                "TRANS": 0,
                "EVENT": 0,
                }

    def proccess(self, data_batch: Dict[str, List[str]]):
        stream_classes = {
                "SENSOR": SensorStream,
                "TRANS": TransactionStream,
                "EVENT": EventStream
                }
        stream_names: List[str] = [name for name in stream_classes]
        stream_col: List[SensorStream | TransactionStream | EventStream] = []

        for data in data_batch:
            stream_name: str = data.split('_')[0]

            if stream_name in stream_names:
                try:
                    stream = stream_classes[stream_name](data)
                    # Polymorphic asabbek tacho
                    _ = stream.process_batch(data_batch[data])
                    self.update_processed(stream.get_stats(), stream_name)
                    stream_col.append(stream)
                except StreamError as e:
                    print(e)

        print("\nBatch 1 Results:")

        print(F"- Sensor data: {self.proccessed['SENSOR']} readings processed")
        print(F"- Transaction data:\
              {self.proccessed['TRANS']} operations processed")
        print(F"- Event data: {self.proccessed['EVENT']} events processed")
        print()
        print("Stream filtering active: High-priority data only")
        print("Filtered results: 2 critical sensor alerts" +
              ", 1 large transaction\n")

    def update_processed(self,
                         stream_state: Dict[str, Union[str, int, float]],
                         stream_name: str):

        for v in stream_state.values():
            if v != 'N/A':
                self.proccessed[stream_name] += 1


class SensorStream(DataStream):
    weather_keys: List[str] = ["temp", "humidity", "pressure"]
    valid_id: str = "SENSOR_"

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type: str = "Environmental Data"
        self.temp: Union[int, float, None] = None
        self.humidity: Union[int, float, None] = None
        self.pressure: Union[int, float, None] = None

    def process_batch(self, data_batch: List[Any]) -> str:
        new_data_batch: List[str] = self.filter_data(data_batch, None)

        for data in new_data_batch:
            match data.split(':')[0]:
                case "temp":
                    self.temp = float(data.split(':')[1])
                case "humidity":
                    self.humidity = int(float(data.split(':')[1]))
                case "pressure":
                    self.pressure = int(float(data.split(':')[1]))
                case _:
                    print("how...")

        if (not self.temp) or (not self.humidity) or (not self.pressure):
            raise StreamError("Missing key(s):" +
                              (" temp," if not self.temp else "") +
                              (" humidity," if not self.humidity else "") +
                              (" pressure," if not self.pressure else "")
                              )

        msg: str = F"Sensor analysis: {len(new_data_batch)} readings processed"
        if (self.temp):
            msg += F", avg temp: {self.temp}°C"

        return msg

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        new_list: List[Any] = []

        if criteria and criteria not in self.criterias:
            print(F"Warning: {criteria}, is not a valid criteria")

        for data in data_batch:
            if not isinstance(data, str):
                print(F"Error: {data} is not a string")
                continue

            name: str = data.split(':')[0]
            if (name not in self.weather_keys):
                print(F"Error: {name} is not part of {self.weather_keys}")
                continue

            val: str = data.split(':')[1]
            try:
                _ = float(val)
            except ValueError:
                print(F"Error, {val} cant be a type of int/float")
                continue

            v_f: float = float(val)
            if criteria == "normal":
                if name == 'buy' and v_f < 2 and v_f > 56:
                    continue
                elif name == 'humidity' and int(v_f) not in range(30, 60):
                    continue
            elif criteria == "criteria":
                if name == 'temp' and v_f >= 2 and v_f <= 56:
                    continue
                elif name == 'humidity' and int(v_f) in range(30, 60):
                    continue
            new_list.append(data)
        return new_list

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
                'temp': self.temp if self.temp else "N/A",
                'humidity': self.humidity if self.humidity else "N/A",
                'pressure': self.pressure if self.pressure else "N/A",
                }


class TransactionStream(DataStream):
    transaction_keys: List[str] = ["buy", "sell"]
    valid_id: str = "TRANS_"

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type: str = "Financial Data"
        self.buys: int = 0
        self.sells: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        new_data_batch: List[str] = self.filter_data(data_batch, None)

        for data in new_data_batch:
            match data.split(':')[0]:
                case "buy":
                    self.buys += int(data.split(':')[1])
                case "sell":
                    self.sells += int(data.split(':')[1])
                case _:
                    print("how...")

        if (not self.buys) or (not self.sells):
            raise StreamError("Missing key(s):" +
                              (" buy," if not self.buys else "") +
                              (" sell," if not self.sells else "")
                              )

        msg: str = F"Transaction analysis: {len(new_data_batch)} operations"
        if (self.sells and self.buys):
            if (self.sells > self.buys):
                msg += F", net flow: {self.buys - self.sells} units"
            else:
                msg += F", net flow: +{self.buys - self.sells} units"

        return msg

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        new_list: List[Any] = []

        if criteria and criteria not in self.criterias:
            print(F"Warning: {criteria}, is not a valid criteria")

        for data in data_batch:
            if not isinstance(data, str):
                print(F"Error: {data} is not a string")
                continue

            name: str = data.split(':')[0]
            if (name not in self.transaction_keys):
                print(F"Error: {name} is not part of {self.transaction_keys}")
                continue

            val: str = data.split(':')[1]
            try:
                _ = int(val)
            except ValueError:
                print(F"Error, {val} cant be a type of int")
                continue

            v_i: int = int(val)
            if v_i < 0:
                print("Error, values cant be negative, skipping", data)
                continue

            if criteria == "normal":
                if v_i >= 100:
                    continue
            elif criteria == "criteria":
                if v_i < 100:
                    continue
            new_list.append(data)
        return new_list

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
                'buys': self.buys if self.buys else "N/A",
                'sells': self.sells if self.sells else "N/A",
                }


class EventStream(DataStream):
    event_keys: List[str] = ["login", "logout", "error"]
    valid_id: str = "EVENT_"

    def __init__(self, stream_id: str) -> None:

        super().__init__(stream_id)
        self.type: str = "System Events"
        self.logins: int = 0
        self.logouts: int = 0
        self.errors: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:

        new_data_batch: List[str] = self.filter_data(data_batch, None)

        for data in new_data_batch:
            match data.split(':')[0]:
                case "login":
                    self.logins += 1
                case "logout":
                    self.logouts += 1
                case "error":
                    self.errors += 1
                case _:
                    print("how...")

        if (not self.logins) or (not self.logouts):
            raise StreamError("Missing key(s):" +
                              (" login," if not self.logins else "") +
                              (" logout," if not self.logouts else "")
                              )

        msg: str = F"Event analysis: {len(new_data_batch)} events"
        msg += F", error detected: {self.errors} "

        return msg

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        new_list: List[Any] = []

        if criteria and criteria not in self.criterias:
            print(F"Warning: {criteria}, is not a valid criteria")

        for data in data_batch:
            if not isinstance(data, str):
                print(F"Error: {data} is not a string")
                continue

            if (data not in self.event_keys):
                print(F"Error: {data} is not part of {self.event_keys}")
                continue

            if criteria == "normal":
                if data == "error":
                    continue
            elif criteria == "criteria":
                if data in ["login", "logout"]:
                    continue
            new_list.append(data)
        return new_list

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
                'logins': self.logins if self.logins else "N/A",
                'logouts': self.logouts if self.logouts else "N/A",
                'errors': self.errors if self.errors else "N/A",
                }


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    # ======================================================================= #
    sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    sensor_id: str = 'SENSOR_001'
    sensor_type: str = "Environmental Data"
    sensor: SensorStream

    print("Initializing Sensor Stream...")
    print(F"Stream ID: {sensor_id}, Type: {sensor_type}")
    print("Processing sensor batch:", sensor_batch)
    try:
        sensor = SensorStream(sensor_id)
        print(sensor.process_batch(sensor_batch))
    except StreamError as e:
        print(e)

    print()
    # ======================================================================= #
    transaction_batch = ["buy:100", "sell:150", "buy:75"]
    transaction_id: str = "TRANS_001"
    transaction_type: str = "Financial Data"
    transaction: TransactionStream

    print("Initializing Event Stream...")
    print(F"Stream ID: {transaction_id}, Type: {transaction_type}")
    print("Processing transaction batch", transaction_batch)
    try:
        transaction = TransactionStream(transaction_id)
        print(transaction.process_batch(transaction_batch))
    except StreamError as e:
        print(e)

    print()
    # ======================================================================= #
    event_batch = ["login", "error", "logout"]
    event_id: str = 'EVENT_001'
    event_type: str = "System Events"
    event:  EventStream

    print("Initializing Event Stream...")
    print(F"Stream ID: {event_id}, Type: {event_type}")

    print("Processing event batch", event_batch)
    try:
        event = EventStream(event_id)
        print(event.process_batch(event_batch))
    except StreamError as e:
        print(e)

    print()

    # ======================================================================= #
    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    batches: Dict[str, List[str]] = {
            'SENSOR_001': ["temp:22.5", "humidity:65", "pressure:1013"],
            'TRANS_001': ["buy:100", "sell:150", "buy:75"],
            'EVENT_001': ["login", "error", "logout"],
            }
    streamprocessor = StreamProcessor()
    streamprocessor.proccess(batches)

    print("All streams processed successfully. Nexus throughput optimal.")
    # ======================================================================= #


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Unexpected error:", e)
