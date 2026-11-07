"""Waitlist for full courses (issue #14). Not wired into booking yet."""

from collections import deque
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class WaitlistEntry:
    user_id: int
    course_id: int
    joined_at: datetime = field(default_factory=datetime.utcnow)


class Waitlist:
    """In-memory FIFO queue per course. TODO: persist it (own table, or a column on courses?)."""

    def __init__(self) -> None:
        self._queues: dict[int, deque[WaitlistEntry]] = {}

    def join(self, user_id: int, course_id: int) -> WaitlistEntry:
        entry = WaitlistEntry(user_id, course_id)
        self._queues.setdefault(course_id, deque()).append(entry)
        return entry

    def pop_next(self, course_id: int) -> WaitlistEntry | None:
        queue = self._queues.get(course_id)
        return queue.popleft() if queue else None
