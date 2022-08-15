import dataclasses


@dataclasses.dataclass
class TwitterUser:
    followers: int
    following: int
    description: str
    username: str
