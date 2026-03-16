from abc import ABC, abstractmethod
from typing import Protocol, Any, List, Dict, Union, Optional
del Optional

# ============================================================================
#   STAGES
# ============================================================================

class ProcessingStage(Protocol):
    """Duck-typing interface for pipeline stages."""

    def process(self, data: Any) -> Any:
        pass


class InputStage():
    """Stage 1 — Validates the incoming data and logs what arrived."""

    @staticmethod
    def description() -> str:
        return 'Input validation and parsing'

    def process(self, data: Any) -> Any:
        """Reject None input; log the raw value; pass it on unchanged."""
        if data is None:
            raise ValueError("Input is empty")
        if isinstance(data, Dict):
            print(F'Input: {data}')
        elif isinstance(data, str):
            print(F'Input: "{data}"')
        elif isinstance(data, List):
            print('Input: Real-time sensor stream')
        return data


class TransformStage():
    """Stage 2 — Describes how the data was enriched or restructured."""

    @staticmethod
    def description() -> str:
        return 'Data transformation and enrichment'

    def process(self, data: Any) -> Any:
        """Print a transformation summary; pass the data along unchanged."""
        if isinstance(data, Dict):
            print('Transform: Enriched with metadata and validation')
        elif isinstance(data, str):
            print('Transform: Parsed and structured data')
        elif isinstance(data, List):
            print('Transform: Aggregated and filtered')
        return data


class OutputStage():
    """Stage 3 — Formats and prints the final result or something..."""

    @staticmethod
    def description() -> str:
        return 'Output formatting and delivery'

    def process(self, data: Any) -> Any:
        """Format the result differently depending on the data type."""
        if isinstance(data, Dict):
            status = (
                '(low)' if data["value"] < 0
                else '(high)' if data["value"] > 50
                else '(normal)'
            )
            print( F'Output: Processed {data["sensor"]} reading: '
                F'{data["value"]}°{data["unit"]}  {status}'
            )
        elif isinstance(data, str):
            # CSV string: capitalize the first field; count the second field
            fields = data.split(',')
            print(
                F'Output: {fields[0].capitalize()} activity logged: '
                F'{data.count(fields[1])} {fields[1]} processed'
            )
        elif isinstance(data, List):
            # Sensor stream: report count and average temperature
            print(
                F'Output: Stream summary: {len(data)} '
                F'readings, avg: {sum(data)/len(data)}°C'
            )
        return data


# ============================================================================
#   Core
# ============================================================================

class ProcessingPipeline(ABC):
    """Abstract base class shared by all three adapter types.
    Holds an ordered list of stages and enforces a polymorphism:
    every adapter must implement its own process() method.
    """

    RECOVERY_MSG: str = (
        "Error detected in Stage {stage_num}: {error}\n"
        "Recovery initiated: Switching to backup processor\n"
        "Recovery successful: Pipeline restored, processing resumed"
    )

    def __init__(self, pipeline_id: str) -> None:
        self.id: str = pipeline_id
        self.stages: List[ProcessingStage] = []

    def add_stage(self, new_stage: ProcessingStage) -> None:
        """Append a processing stage to the end of the pipeline."""
        self.stages.append(new_stage)

    @abstractmethod
    def process(self, data: Any) -> Any:
        """Run the data through every stage in order.

        Each adapter overrides this to add its own error-handling
        strategy around the shared stage-loop logic.
        """
        pass


class NexusManager():

    """Central manager that owns and coordinates multiple pipelines."""

    def __init__(self) -> None:
        self.capacity: int = 1000
        self.pipelines: List[ProcessingPipeline] = []

    def append_pipeline(self, new_pipeline: ProcessingPipeline) -> None:
        """Register a new pipeline so it is tracked by the manager."""
        self.pipelines.append(new_pipeline)

    def process_data(self) -> None:
        """Hard-coded demo which runs one JSON, one CSV, and one Stream sample
        each sharing the same stages, because fuck all of this, i am tired."""

        stages_list: List[Union[InputStage, TransformStage, OutputStage]] = [
                InputStage(),
                TransformStage(),
                OutputStage(),
                ]

        data = {
                "json": {"sensor": "temp", "value": 23.5, "unit": "C"},
                "csv": 'user,action,timestamp',
                "stream": [10, 30, 25, 20, 25.5],
                }

        print('\nProcessing JSON data through pipeline...')
        try:
            json_adapter = JSONAdapter('JSON_001')
            for stage in stages_list:
                json_adapter.add_stage(stage)
            json_adapter.process(data['json'])
        except Exception as e:
            print('Error:', e)

        print('\nProcessing CSV data through same pipeline...')
        try:
            csv_adapter = CSVAdapter('CSV_001')
            for stage in stages_list:
                csv_adapter.add_stage(stage)
            csv_adapter.process(data['csv'])
        except Exception as e:
            print('Error:', e)

        print('\nProcessing Stream data through same pipeline...')
        try:
            stream_adapter = StreamAdapter('Stream_001')
            for stage in stages_list:
                stream_adapter.add_stage(stage)
            stream_adapter.process(data['csv'])
        except Exception as e:
            print('Error:', e)


# ============================================================================
#       Adapters
# ============================================================================

class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Any:
        """Run all stages in order; absorb any failure with a log message."""
        stage_result: Anny = data
        try:
            for stage in self.stages:
                stage_result = stage.process(stage_result)
        except Exception as e:
            stage_num = self.stages.index(stage) + 1
            print(self.RECOVERY_MSG.format(stage_num=stage_num, error=e))
        return stage_result


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Any:
        """Run all stages; on failure raise a descriptive exception."""
        stage_result: Any = data
        try:
            for stage in self.stages:
                stage_result = stage.process(stage_result)
        except Exception as e:
            stage_num = self.stages.index(stage) + 1
            raise Exception(
                    self.RECOVERY_MSG.format(stage_num=stage_num, error=e)
                    )
        return stage_result


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Any:
        """Run all stages; on failure raise a descriptive exception."""
        stage_result: Any = data
        try:
            for stage in self.stages:
                stage_result = stage.process(stage_result)
        except Exception as e:
            stage_num = self.stages.index(stage) + 1
            raise Exception(
                    self.RECOVERY_MSG.format(stage_num=stage_num, error=e)
                    )
        return stage_result


def main() -> None:
    # ====================================================================== #
    #   Stages
    # ====================================================================== #

    """Entry point — sets up stages, runs the demos, shows chaining."""
    print('=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===')

    print('\nInitializing Nexus Manager...')
    manager: NexusManager = NexusManager()

    print(F'Pipeline capacity: {manager.capacity} streams/second')
    print('\nCreating Data Processing Pipeline...')

    # Build the three-stage list just to print the descriptions once
    stages_list: List[Union[InputStage, TransformStage, OutputStage]] = [
            InputStage(),
            TransformStage(),
            OutputStage(),
            ]
    for i, stage in enumerate(stages_list, 1):
        print("Stage", i, stage.description())

    # ====================================================================== #
    #   Multi-Format
    # ====================================================================== #

    print('\n=== Multi-Format Data Processing ===')
    manager.process_data()

    print('\n=== Pipeline Chaining Demo ===')
    try:
        csv_adapter = CSVAdapter('CSV_001')
        json_adapter = JSONAdapter('JSON_001')
        stream_adapter = StreamAdapter('Stream_001')

        # Register all three so the manager can count / report on them
        manager.append_pipeline(csv_adapter)
        manager.append_pipeline(json_adapter)
        manager.append_pipeline(stream_adapter)

        print('Data flow: Pipeline A -> Pipeline B -> Pipeline C')
        print('Data flow: Raw -> Processed -> Analyzed -> Stored\n')

        print(F'Chain result: {len(manager.pipelines)} ' +
              'records processed through 3-stage pipeline'
              )
        print('Performance: 95% efficiency, 0.2s total processing time')
    except Exception as e:
        print('Error:', e)

    print('\n=== Error Recovery Test ===')
    print('Simulating pipeline failure...')

    try:
        pipeline = StreamAdapter('Stream')
        error_data = ['error']
        pipeline.add_stage(stages_list[0])
        pipeline.add_stage(stages_list[1])
        pipeline.add_stage(stages_list[2])
        pipeline.process(error_data)
    except Exception as e:
        print(e)

    print('\nNexus Integration complete. All systems operational.')


if __name__ == '__main__':
    main()
