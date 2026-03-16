from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod
del Optional, Dict


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        ''' Process the data and return result string '''
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ''' Validate if data is appropriate for this processor '''
        pass

    def format_output(self, result: str) -> str:
        ''' Format the output string pass '''
        # print(result)
        print("Output:", end=' ')
        if (result[0:6] == "ERROR:"):
            return ("[ALERT] ERROR level detected:"+result[6:])
        else:
            return (result)


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        print("Processing data:", data)
        if (self.validate(data)):
            print("Validation: Numeric data verified")
            if isinstance(data, list):
                result = self.format_output(
                        F"Processed {len(data)} numeric values, " +
                        F"sum={sum(data)}, " +
                        F"avg={sum(data)/len(data)}")
                return result
            else:
                result = self.format_output(
                        "Processed 1 numeric values, " +
                        F"sum={data}, " +
                        F"avg={data}")
                return result
        else:
            error: str = "ERROR: Validation: Bad numeric data found!"
            print(error)
            return (self.format_output(error))

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for data_ in data:
                if not isinstance(data_, (int, float)):
                    return False
        elif not isinstance(data, (int, float)):
            return False
        return True

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        print(F'Processing data: "{data}"')
        if self.validate(data):
            print("Validation: Text data verified")
            result = self.format_output(
                    F"Processed {len(data)} characters, " +
                    F"{len(data.split())} words")
            return (result)
        else:
            error: str = "ERROR: Validation: Bad text data recieved!"
            print(error)
            return (self.format_output(error))

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        print(F'Processing data: "{data}"')
        if self.validate(data):
            print("Validation: Log entry verified")
            return (self.format_output(data))
        else:
            error: str = "ERROR: Validation: Bad log format recieved!"
            print(error)
            return (self.format_output(error))

    def validate(self, data: Any) -> bool:
        if isinstance(data, str) and (
                data.split(':')[0] == "ERROR"
                or data.split(':')[0] == "LOG"):
            return True
        return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)


def main() -> None:

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    # ========================================================================
    print("Initializing Numeric Processor...")

    numProccess = NumericProcessor()
    num_data: List[Union[int, float]] = [1, 2, 3, 4, 5]
    print(numProccess.process(num_data), end='\n\n')

    # ========================================================================
    print("Initializing Text Processor...")

    txtProcessor = TextProcessor()
    txt_data: str = "Hello Nexus World"
    print(txtProcessor.process(txt_data), end='\n\n')

    # ========================================================================
    print("Initializing Log Processor...")

    logProcessor = LogProcessor()
    log_data: str = "ERROR: Connection timeout"
    # log_data: str = "LOG: Connection timeout"
    print(logProcessor.process(log_data), end='\n\n')


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Unexpected error:", e)
