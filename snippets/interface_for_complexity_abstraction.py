from abc import ABC, abstractmethod
from datetime import datetime


# Define an interface for slot services
class SlotService(ABC):
    @abstractmethod
    def check_availability(self, date_time):
        pass

    @abstractmethod
    def book_slot(self, date_time):
        pass


# Use it as a simple interface
def book_any_available_slot(slot_service: SlotService, booking_time: datetime) -> None:
    available = slot_service.check_availability(booking_time)
    if available:
        slot_service.book_slot(booking_time)


book_any_available_slot(ReallyComplexOrExternalSlotService(), datetime.now())
