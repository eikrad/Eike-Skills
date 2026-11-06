# Clubhouse

Booking app for Vesterbro Tennis & Padel Club. Members and guests book courses (group lessons with a fixed number of spots) and courts.

Stack: Python 3.12, FastAPI, PostgreSQL through SQLAlchemy. Emails go through `src/notify/`.

The courses table is deployed and read directly by two reporting clients maintained by other teams. The waitlist storage contract in this release must be supported by those clients; changing it after release requires persisted-data migration and coordinated client changes.
