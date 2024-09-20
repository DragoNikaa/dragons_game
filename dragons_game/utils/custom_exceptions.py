class DragonError(Exception):
    def __init__(self, message: str, dragon_name: str):
        super().__init__(message)
        self.dragon_name = dragon_name


class DragonNotOwnedError(DragonError):
    def __init__(self, dragon_name: str):
        super().__init__(f"User does not own dragon '{dragon_name}'", dragon_name)


class DragonAlreadyOwnedError(DragonError):
    def __init__(self, dragon_name: str):
        super().__init__(f"User already owns dragon '{dragon_name}'", dragon_name)


class DragonAlreadyInTeamError(DragonError):
    def __init__(self, dragon_name: str):
        super().__init__(f"Dragon '{dragon_name}' is already in team", dragon_name)


class TooManyDragonsError(DragonError):
    def __init__(self, max_dragons: int):
        super().__init__(f'Cannot add more than {max_dragons} dragons to team', '')
        self.max_dragons = max_dragons


class DragonHealthError(DragonError):
    def __init__(self, dragon_name: str):
        super().__init__(f"Dragon '{dragon_name}' has no health left", dragon_name)


class DragonEnergyError(DragonError):
    def __init__(self, dragon_name: str, current_energy: int):
        super().__init__(f"Dragon '{dragon_name}' has {current_energy} current energy", dragon_name)


class SectionError(Exception):
    def __init__(self, element_name: str, message: str):
        super().__init__(message)
        self.element_name = element_name


class ElementNotInSectionError(SectionError):
    def __init__(self, element_name: str):
        super().__init__(element_name, f"Element '{element_name}' not found in section")


class ElementAlreadyInSectionError(SectionError):
    def __init__(self, element_name: str):
        super().__init__(element_name, f"Element '{element_name}' is already in section")


class IncorrectMethodError(SectionError):
    def __init__(self, element_name: str, element_type: type):
        super().__init__(element_name,
                         f"For element '{element_name}' method 'get_{element_type.__name__.lower()}' should be used")
        self.element_type = element_type


class ElementTypeError(SectionError):
    def __init__(self, element_name: str, expected_types: tuple[type, ...]):
        types = ', '.join([f"'{expected_type.__name__}'" for expected_type in expected_types])
        super().__init__(element_name,
                         f"Element '{element_name}' must be instance of one of following classes: {types}")
        self.expected_types = expected_types
