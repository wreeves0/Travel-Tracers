steps = [
    [
        """
        CREATE TABLE IF NOT EXISTS accounts (
            id SERIAL PRIMARY KEY NOT NULL,
            email VARCHAR(200) NOT NULL,
            password VARCHAR(200) NOT NULL,
            full_name VARCHAR(250) NOT NULL
        );
        """,
        """
        DROP TABLE accounts;
        """,
    ],
]
