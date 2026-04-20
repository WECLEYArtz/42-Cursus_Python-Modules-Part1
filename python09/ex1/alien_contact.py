from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing_extensions import Self
from enum import Enum
import json


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field(default_factory=datetime.now)
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType = Field(default_factory=ContactType)
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validator(self) -> Self:
        if not self.contact_id[0:2] == 'AC':
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if (self.contact_type == ContactType.TELEPATHIC
                and self.witness_count < 3):
            raise ValueError(
                    "Telepathic contact requires at least 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                    "Strong signals (> 7.0) should include received messages")
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

    good_test = "generated_data/alien_contacts.json"
    with open(good_test) as f:
        aliencontact = json.load(f)
        show(AlienContact(**aliencontact[0]))

    print("\n======================================")
    print("Expected validation error:")

    bad_test = "generated_data/invalid_contacts.json"
    with open(bad_test) as f:
        aliencontact = json.load(f)
        show(AlienContact(**aliencontact[0]))


if __name__ == "__main__":
    try:
        main()
    except ValidationError as e:
        value_error_msg = e.errors()[0].get("ctx").get("error")
        if value_error_msg:
            print(value_error_msg)
        else:
            print(e.errors()[0]['msg'])
    except PermissionError:
        print("stop missing with the file bro")
    except Exception as e:
        print(e)
