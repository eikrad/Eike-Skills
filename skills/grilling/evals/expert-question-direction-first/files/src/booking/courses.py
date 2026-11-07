"""Course booking.

Booking a spot locks the course row (SELECT ... FOR UPDATE) so two people
can't take the last spot at the same time.
"""

from sqlalchemy import select

from .models import Booking, Course


class CourseFull(Exception):
    pass


def book_spot(session, course_id: int, user_id: int) -> Booking:
    course = session.execute(
        select(Course).where(Course.id == course_id).with_for_update()
    ).scalar_one()
    if course.booked >= course.capacity:
        raise CourseFull(course_id)
    course.booked += 1
    booking = Booking(course_id=course_id, user_id=user_id)
    session.add(booking)
    return booking


def cancel_spot(session, course_id: int, user_id: int) -> None:
    course = session.execute(
        select(Course).where(Course.id == course_id).with_for_update()
    ).scalar_one()
    session.query(Booking).filter_by(course_id=course_id, user_id=user_id).delete()
    course.booked -= 1
