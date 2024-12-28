from dataclasses import dataclass, asdict

@dataclass
class TimeEntry():
    project:str = None
    client:str = None
    description: str = None
    duration: float = None
    created_at:str = None

    def make_dict(self):
        return asdict(self)