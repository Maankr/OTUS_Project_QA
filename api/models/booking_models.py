from pydantic import BaseModel
from api.models.common_models import BookingDates


class BookingRequest(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str | None = None

class BookingResponse(BaseModel):
    bookingid: int
    booking: BookingRequest