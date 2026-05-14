from deque_custom import Deque
from action_manager import UndoRedoSystem


# =========================
# TESTS DE DEQUE
# =========================

def test_deque():
    dq = Deque()

    assert dq.is_empty() is True

    dq.add_rear(10)
    dq.add_front(5)

    assert dq.size() == 2
    assert dq.remove_front() == 5
    assert dq.remove_rear() == 10

    assert dq.is_empty() is True


# =========================
# TESTS UNDO/REDO
# =========================

def test_undo_redo():
    system = UndoRedoSystem()

    system.add_action("Escribir Hola")
    system.add_action("Agregar Mundo")

    assert len(system.get_current_state()) == 2

    system.undo()

    assert len(system.get_current_state()) == 1

    system.redo()

    assert len(system.get_current_state()) == 2


# =========================
# CASOS LÍMITE
# =========================

def test_empty_action():
    system = UndoRedoSystem()

    try:
        system.add_action("")
    except ValueError:
        assert True


def test_undo_empty():
    system = UndoRedoSystem()

    try:
        system.undo()
    except Exception:
        assert True


def test_redo_empty():
    system = UndoRedoSystem()

    try:
        system.redo()
    except Exception:
        assert True


if __name__ == "__main__":
    test_deque()
    test_undo_redo()
    test_empty_action()
    test_undo_empty()
    test_redo_empty()

    print("Todos los tests pasaron correctamente")