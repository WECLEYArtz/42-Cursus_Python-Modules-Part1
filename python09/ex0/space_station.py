from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = Field(default_factory=datetime.now)
    is_operational: bool = Field(default=True)
    notes: str | None = Field(max_length=200, default=None)


def show(sp_st: SpaceStation) -> None:
    print("Valid station created:")
    print("ID:", sp_st.station_id)
    print("Name:", sp_st.name)
    print("Crew: ", sp_st.crew_size, "people")
    print(f"Power: {sp_st.power_level}%")
    print(f"Oxygen: {sp_st.oxygen_level}%")
    print("Status:", '' if sp_st.is_operational else "Not", "Operational")


def main() -> None:
    try:
        print("Space Station Data Validation")
        print("========================================")
        space_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
            is_operational=True,
            notes="isthisamongus")
        show(space_station)

        print("\n========================================")
        _ = SpaceStation(
                station_id="12345678",
                name="smiya",
                crew_size=21,
                power_level=50.0,
                oxygen_level=50.0,
                last_maintenance=datetime.now(),
                is_operational=True,
                notes="isthisamongus")
    except ValidationError as e:
        print("Expected validation error:")
        for e in e.errors():
            print(e['msg'])


if __name__ == "__main__":
    try:
        main()
    except ValidationError as e:
        for e in e.errors():
            print(e['msg'])
    except Exception as e:
        print(e)
