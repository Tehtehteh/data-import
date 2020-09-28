from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    rmq_user: str = "guest"
    rmq_password: str = "guest"
    rmq_host: str = "localhost"
    refetch_time: int = 60*5  # refetch 5 minutes

    @property
    def rmq_connection_string(self):
        return f'amqp://{self.rmq_user}:{self.rmq_password}@{self.rmq_host}'
