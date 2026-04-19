from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str | None] = Field(max_length=200)


def main() -> None:
    data: dict[str, str] = {
            "station_id": "12345678",
            "name": "smiya",
            "crew_size": '2',
            "power_level": '50.0',
            "oxygen_level": '50.0',
            "last_maintenance": str(datetime.now()),
            "is_operational": 't',
            "notes": "is this amongus"

            }
    space_station = SpaceStation(**data)
    show(space_station)

    print("========================================")
    print("Expected validation error:")
    try:
        data['crew_size'] = '21'
        _ = SpaceStation(**data)
    except ValidationError as e:
        print(e.errors()[0]['msg'])


def show(sp_st: SpaceStation) -> None:
    print("Space Station Data Validation")
    print("========================================")
    print("Valid station created:")
    print("ID:", sp_st.station_id)
    print("Name:", sp_st.name)
    print("Crew: ", sp_st.crew_size, "people")
    print(f"Power: {sp_st.power_level}%")
    print(f"Oxygen: {sp_st.power_level}%")
    print("Status:", "" if sp_st.is_operational else "Not", "Operational")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
