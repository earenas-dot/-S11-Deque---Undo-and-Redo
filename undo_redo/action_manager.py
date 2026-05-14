from deque_custom import Deque


class UndoRedoSystem:
    def __init__(self):
        self.undo_stack = Deque()
        self.redo_stack = Deque()
        self.current_state = []

    def add_action(self, action):
        action = action.strip()

        if not action:
            raise ValueError("La acción no puede estar vacía")

        self.undo_stack.add_rear(action)
        self.current_state.append(action)

        # Limpiar historial redo
        self.redo_stack = Deque()

    def undo(self):
        if self.undo_stack.is_empty():
            raise Exception("No hay acciones para deshacer")

        action = self.undo_stack.remove_rear()

        self.redo_stack.add_rear(action)

        if self.current_state:
            self.current_state.pop()

        return action

    def redo(self):
        if self.redo_stack.is_empty():
            raise Exception("No hay acciones para rehacer")

        action = self.redo_stack.remove_rear()

        self.undo_stack.add_rear(action)
        self.current_state.append(action)

        return action

    def get_history(self):
        return self.undo_stack.get_items()

    def get_redo_history(self):
        return self.redo_stack.get_items()

    def get_current_state(self):
        return self.current_state.copy()