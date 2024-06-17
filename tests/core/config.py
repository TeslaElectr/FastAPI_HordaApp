class Settings:

    def __init__(
        self,
        DB_URL: str = "postgresql+asyncpg://user:example@localhost:5432/hdb_test",
        DB_ECHO: bool = True,
        expire_on_commit: bool = False,
        DB_max_overflow: int = 50,
        DB_pool_size: int = 50,
        ):

        self.DB_URL = DB_URL
        self.DB_ECHO = DB_ECHO
        self.DB_max_overflow = DB_max_overflow
        self.DB_pool_size = DB_pool_size
        self.expire_on_commit = expire_on_commit

        
settings = Settings()
