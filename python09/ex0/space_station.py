from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
import json


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = Field(default_factory=datetime.now)
    is_operational: bool = Field(default=True)
    notes: str | None = Field(max_length=200)


def show(sp_st: SpaceStation) -> None:
    print("Valid station created:")
    print("ID:", sp_st.station_id)
    print("Name:", sp_st.name)
    print("Crew: ", sp_st.crew_size, "people")
    print(f"Power: {sp_st.power_level}%")
    print(f"Oxygen: {sp_st.power_level}%")
    print("Status:", "" if sp_st.is_operational else "Not", "Operational")


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")

    good_test = "generated_data/space_stations.json"
    with open(good_test) as f:
        space_station = json.load(f)
        show(SpaceStation(**space_station[0]))

    print("\n========================================")
    print("Expected validation error:")

    bad_test = "generated_data/invalid_stations.json"
    with open(bad_test) as f:
        space_station = json.load(f)
        show(SpaceStation(**space_station[0]))


if __name__ == "__main__":
    try:
        main()
    except ValidationError as e:
        print(e.errors()[0]['msg'])
    except PermissionError:
        print("stop missing with the file bro")
    except Exception as e:
        print(e)
