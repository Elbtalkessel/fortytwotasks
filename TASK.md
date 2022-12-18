Application overview
----
Time tracking and user expectation management.
On main page user can set when he plans to complete a task. On the same page user can see his active ETA and past 10
ETA.
On second page user can see all active ETA.

## ETA syntax

To start timer: `<project>#<issue-num> at [today | tomorrow | MM-DD] HH:MM`. Examples:

```
foo#1 at 20:00
foo#1 at tomorrow 20:00
foo#1 at 01-01 20:00
```

To extend ETA: `eta +<num>[m | h | d]`. Examples:

```
# plus minute
eta +1m
# plus hour
eta +1h
# plus day
eta +1d
```

To close ETA: `eta done`.

## ETA rules

- Allowed only 1 active ETA per user, if user wants start on another issue, he must close current one.
- Expected time to finish shall be greater than current time.
- Datetime should be stored in UTC, but to user must be presented on his local time.

## DB Tables:

Expectations:

- created_at: non-nullable timestamp, current timestamp is default value.
- expected_at: non-nullable timestamp.
- done_at: nullable timestamp.
- issue: non-blank var char field, 100 symbols max.
- user: FK to User.
- project: FK to Project.

User(AbstractUserModel)

Project:

- name: non-blank var char field, 100 symbols max.

All tables must be registered in admin panel.

## Frontend

3 UI pages: Login, Open ETA, All ETA.

### Login / Registration

Just ask username and password for sign-in or log-in.

### Open ETA

On the page user can see his past ETAs (closed ETAs, up to 10) and current ETA as last entry in table (if any).
Example of the ETA table:

| PROJECT | ISSUE | STARTED AT       | COMPLETED AT     |
|---------|-------|------------------|------------------|
| foo     | 1     | 2020-01-01 10:00 | 2020-01-01 14:00 |
| foo     | 2     | 2020-01-01 15:00 | 2020-01-01 17:00 |
| bar     | 1     | 2020-01-01 17:00 |                  |

Below the table add an input field.
Command input must validate command and show errors, if any. See [rules](#eta-rules) and [syntax](#eta-syntax).

### All ETA

On the page user can see all OPEN ETAs. Example:

| USER  | PROJECT | ISSUE | STARTED AT       | EXPECTED AT      |
|-------|---------|-------|------------------|------------------|
| john  | foo     | 30    | 2020-01-01 10:00 | 2020-01-01 15:00 |
| boris | bar     | 32    | 2020-01-01 15:00 | 2020-01-01 16:00 |
