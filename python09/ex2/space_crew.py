from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing_extensions import Self
from enum import Enum
import json


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank = Field(default_factory=Rank)
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field(default_factory=datetime.now)
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)
    specialization: str | None = Field(default=None)

    @model_validator(mode='after')
    def validator(self) -> Self:
        if (self.mission_id[0] != "M"):
            raise ValueError("Mission ID must start with 'M'")
        has_leader: bool = False
        for crewmate in self.crew:
            if crewmate.rank in [Rank.CAPTAIN, Rank.COMMANDER]:
                has_leader = True
        if not has_leader:
            raise ValueError("Must have at least one Commander or Captain")
        if self.duration_days > 365 and self.get_experinced_percentage() < 50:
            raise ValueError(
                    "Long missions (> 365 days)" +
                    "need 50% experienced crew (5+ years)")
        for crew in self.crew:
            if not crew.is_active:
                raise ValueError("All crew members must be active")
        return self

    def get_experinced_percentage(self) -> int:
        crew_count = len(self.crew)
        experinced = len([crew for crew in self.crew
                          if crew.years_experience >= 5])
        return (int(experinced / crew_count * 100))


def show(spacemission: SpaceMission) -> None:
    print("Valid mission created:")

    print("Mission:", spacemission.mission_name)
    print("ID:", spacemission.mission_id)
    print("Destination:", spacemission.destination)
    print(f"Duration: {spacemission.duration_days} days")
    print(f"Budget: ${spacemission.budget_millions}M")
    print("Crew size:", len(spacemission.crew))
    print("Crew members:",)
    for crew in spacemission.crew:
        print(f"- {crew.name} ({crew.rank.value}) - {crew.specialization}")


def main() -> None:
    test = "generated_data/space_missions.json"
    with open(test) as f:
        print("Space Mission Crew Validation")
        print("======================================")

        mission = json.load(f)
        show(SpaceMission(**mission[0]))

        print("\n======================================")
        print("Expected validation error:")
        show(SpaceMission(**mission[4]))


if __name__ == "__main__":
    try:
        main()
    except ValidationError as e:
        value_error_msg = e.errors()[0].get("ctx")
        print(value_error_msg)
        if value_error_msg and value_error_msg.get("error"):
            print(value_error_msg.get("error"))
        else:
            print(e.errors()[0]['msg'])
    except FileNotFoundError:
        print("Make sure the 42 generated Jsons exist, and run from the root")
    except PermissionError:
        print("stop missing with the file bro")
    except Exception as e:
        print(e)
