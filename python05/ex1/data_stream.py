from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):
    def __init__(self, stream_id: str, type: str):
        self.stream_id: str = stream_id
        self.type: str = type
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


class StreamProcessor(DataStream):
    '''
    handles multiple stream types polymorphically
    '''


class SensorStream(DataStream):
    weather_keys: List[str] = ["temp", "humidity", "pressure"]

    def __init__(self, stream_id: str):
        print("Initializing Sensor Stream...")

        type = 'Environmental Data'
        super().__init__(stream_id, type)
        self.temp: Union[int, float, None] = None
        self.humidity: Union[int, float, None] = None
        self.pressure: Union[int, float, None] = None

        print(F"Stream ID: {self.stream_id}, Type: {self.type}")

    def process_batch(self, data_batch: List[Any]) -> str:
        print("Processing sensor batch:", data_batch)

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
            raise ValueError("Missing key(s):" +
                             (" temp," if not self.temp else "") +
                             (" humidity," if not self.humidity else "") +
                             (" pressure," if not self.pressure else "")
                             )

        msg: str = F"Sensor analysis: {len(new_data_batch)} readings processed"
        if (self.temp):
            msg += F", avg temp: {self.temp}°C"
        else:
            msg += ", couldn't parse temp (error)"
        if not self.humidity:
            msg += ", couldn't parse humidity (error)"
        if not self.pressure:
            msg += ", couldn't parse pressure (error)"

        return msg

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:

        new_list: List[Any] = []
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
            val_float: float = float(val)

            if criteria == "normal":
                if name == 'temp' and val_float not in range(2, 56):
                    continue
                elif name == 'humidity' and val_float not in range(30, 60):
                    continue
                elif name == 'pressure' and val_float not in range(1009, 1023):
                    continue
            elif criteria == "criteria":
                if name == 'temp' and val_float in range(2, 56):
                    continue
                elif name == 'humidity' and val_float in range(30, 60):
                    continue
                elif name == 'pressure' and val_float in range(1009, 1023):
                    continue

            new_list.append(data)
        return new_list



    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass


class TransactionStream(DataStream):
    pass


class EventStream(DataStream):
    pass


def main():
    # ======================================================================= #
    sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    sensor = SensorStream('SENSOR_001')
    print(sensor.process_batch(sensor.filter_data(sensor_batch, "normal")))
    print(sensor.process_batch(sensor.filter_data(sensor_batch, "critical")))

    # ======================================================================= #
    # print("Initializing Transaction Stream...")
    #
    # print("Initializing Event Stream...")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Unexpected error:", e)


# $> python3 data_stream.py
# === CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===
#
# Initializing Sensor Stream...
# Stream ID: SENSOR_001, Type: Environmental Data
# Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]
# Sensor analysis: 3 readings processed, avg temp: 22.5°C
#
# Initializing Transaction Stream...
# Stream ID: TRANS_001, Type: Financial Data
# Processing transaction batch: [buy:100, sell:150, buy:75]
# Transaction analysis: 3 operations, net flow: +25 units
#
# Initializing Event Stream...
# Stream ID: EVENT_001, Type: System Events
# Processing event batch: [login, error, logout]
# Event analysis: 3 events, 1 error detected
#
# === Polymorphic Stream Processing ===
# Processing mixed stream types through unified interface...
#
# Batch 1 Results:
# - Sensor data: 2 readings processed
# - Transaction data: 4 operations processed
# - Event data: 3 events processed
#
# Stream filtering active: High-priority data only
# Filtered results: 2 critical sensor alerts, 1 large transaction
#
# All streams processed successfully. Nexus throughput optimal.
