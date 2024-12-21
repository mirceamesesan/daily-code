from dataclasses import dataclass, asdict

@dataclass
class TimeEntry():
    description: str = None
    duration: float = None

    def make_dict(self):
        return asdict(self)