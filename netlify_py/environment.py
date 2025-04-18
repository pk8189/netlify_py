import enum


class Environment(enum.Enum):
    """Pre-defined base URLs for the API"""

    PRODUCTION = "https://api.netlify.com/api/v1"
    MOCK_SERVER = "https://api.sideko.dev/v1/mock/public/netlify/0.1.0"
