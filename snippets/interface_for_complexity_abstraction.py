from abc import ABC, abstractmethod


# Define an interface for slot services
class SlotService(ABC):
    @abstractmethod
    def check_availability(self):
        pass

    @abstractmethod
    def book_slot(self):
        pass


# Use it as a simple interface
def book_any_available_slot(slot_service: SlotService) -> None:
    available = slot_service.check_availability()
    if available:
        slot_service.book_slot()


book_any_available_slot(ReallyComplexSlotService())
