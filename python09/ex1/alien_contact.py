from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing_extensions import Self
from enum import Enum


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validator(self) -> Self:
        if not self.contact_id[0:2] == 'AC':
            raise ValueError()
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError()
        if (self.contact_type == ContactType.TELEPATHIC
                and self.witness_count < 3):
            raise ValueError()
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError()
        return self


def show(aliencontact: AlienContact) -> None:
    print("Valid contact report:")
    print("ID:", aliencontact.contact_id)
    print("Type:", aliencontact.contact_type.value)
    print("Location:", aliencontact.location)
    print(f"Signal: {aliencontact.signal_strength}/10")
    print(f"Duration: {aliencontact.duration_minutes} minutes")
    print("Witnesses:", aliencontact.witness_count)
    print(f"Message: '{aliencontact.message_received}'")


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    aliencontact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True
            )
    show(aliencontact)

    print("\n======================================")
    print("Expected validation error:")

    try:
        _ = AlienContact(
                contact_id="AC_2024_001",
                timestamp=datetime.now(),
                location="Area 51, Nevada",
                contact_type=ContactType.RADIO,
                signal_strength=8.5,
                duration_minutes=45,
                witness_count=1,
                message_received="Greetings from Zeta Reticuli",
                is_verified=True
                )
    except ValidationError as e:
        print(e.errors()[0]['msg'])
    print("Telepathic contact requires at least 3 witnesses")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
