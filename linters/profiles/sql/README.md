# SQL

Use **SQLFluff** with the actual database dialect. Merge `.sqlfluff` into the
project root. This template checks all applicable rules, disables inline `noqa`
suppression and avoids the default large-file skip. Bound CI runtime for large
files; a timeout is a failed check, not permission to omit the file silently.

For a PostgreSQL project with SQL under `sql/`:

```sh
sqlfluff lint --dialect postgres sql/
```

Select the correct dialect for MySQL, SQLite, T-SQL, Oracle, BigQuery, etc. Do not
assume PostgreSQL merely because it appears in this example. `sqlfluff dialects`
lists the installed version's supported dialects. Use the existing dependency
manager to pin SQLFluff and commit its lockfile.

The template uses `raw` for plain SQL. For dbt or Jinja, configure the matching
templater and dependencies, and verify the rendered variants. Never ignore
`parsing` or `templating` errors, use `--nofail`, or enable fixes on unparsable
SQL. Linting does not establish query results, query plans, migration safety or
database permissions; run the relevant database tests too.

Sources: [configuration defaults](https://docs.sqlfluff.com/en/stable/configuration/defaults.html),
[CLI reference](https://docs.sqlfluff.com/en/stable/reference/cli/),
[dialects](https://docs.sqlfluff.com/en/stable/reference/dialects.html).
