# Chinook Database

A popular sample database is the [Chinook Database](https://github.com/lerocha/chinook-database). It is a sample database that contains data about a digital media store, including tables for artists, albums, customers, invoices, and more. It is often used for learning and practicing SQL queries.

The co-located SQL setup files were downloadedfrom the [Chinook Database Releases](https://github.com/lerocha/chinook-database/releases) page:

- [`Chinook_MySql.sql`](https://github.com/lerocha/chinook-database/releases/download/v1.4.5/Chinook_MySql.sql)
- [`Chinook_PostgreSql.sql`](https://github.com/lerocha/chinook-database/releases/download/v1.4.5/Chinook_PostgreSql.sql)
- [`Chinook_Sqlite.sql`](https://github.com/lerocha/chinook-database/releases/download/v1.4.5/Chinook_Sqlite.sql)

Each file can be executed in the corresponding database system to set up the Chinook database.

PostgreSQL:

```bash
psql -U postgres -d chinook -f Chinook_PostgreSql.sql
```

MySQL:

```bash
mysql -u root -p chinook < Chinook_MySql.sql
```

SQLite:

```bash
sqlite3 chinook.db < Chinook_Sqlite.sql
```
