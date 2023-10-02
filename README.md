For start:
* alembic upgrade head
* uvicorn src.main:app --reload


For dev use .env file
```
DB_HOST=127.0.0.1
DB_PORT=5432
DB_USER=postgres
DB_PASS=password
DB_NAME=postgres
```

## Useful scripts:
* Create migration
>  alembic revision --autogenerate -m "Database creations"
* Delete tables from DB:
```sql
drop table alembic_version;
drop table load_test_describe;
drop table load_test_result;
drop table load_test_result_summary ;
drop table product;
* ```

