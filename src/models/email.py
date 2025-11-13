thonclass Email:
    def __init__(self, email: str, is_verified: bool, timestamp: int):
        self.email = email
        self.is_verified = is_verified
        self.timestamp = timestamp