from abc import ABC, abstractmethod

class ModeStrategy(ABC):
    def __init__(self, context):
        self.context = context
        self.quit_flag = False

    @abstractmethod
    def run(self) -> None:
        pass

    @abstractmethod
    def _process_command(self, command: str) -> None:
        pass

    def _get_display_data(self) -> dict:
        return {
            'mode': self.context.mode,
            'class_list': self.context.classes_list.get('classes', []),
            'message': self.context.message
        }