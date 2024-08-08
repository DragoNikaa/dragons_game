class DragonError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class DragonNotOwnedError(DragonError):
    def __init__(self, dragon_name: str):
        super().__init__(f"User does not own dragon '{dragon_name}'")
        self.dragon_name = dragon_name


class DragonAlreadyOwnedError(DragonError):
    def __init__(self, dragon_name: str):
        super().__init__(f"User already owns dragon '{dragon_name}'")
        self.dragon_name = dragon_name


class DragonAlreadyInTeamError(DragonError):
    def __init__(self, dragon_name: str):
        super().__init__(f"Dragon '{dragon_name}' is already in team")
        self.dragon_name = dragon_name


class TooManyDragonsError(DragonError):
    def __init__(self, max_dragons: int):
        super().__init__(f'Cannot add more than {max_dragons} dragons to team')
        self.max_dragons = max_dragons


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
