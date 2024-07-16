import pygame

from dragons_game.elements.button import Button
from dragons_game.elements.image import Image
from dragons_game.game_states.main_menu.configuration.background import BackgroundConfig
from dragons_game.game_states.main_menu.configuration.level_buttons import Island1EasyLevelButtonConfig, \
    Island1MediumLevelButtonConfig, Island1HardLevelButtonConfig, Island1FiendishLevelButtonConfig
from dragons_game.game_states.main_menu.configuration.top_and_bottom_buttons import TrophiesButtonConfig, \
    TrophiesButtonImageConfig, TrophiesButtonTextConfig, TrophiesButtonTextBorderConfig, EggsButtonConfig, \
    EggsButtonImageConfig, EggsButtonTextConfig, EggsButtonTextBorderConfig, FishButtonConfig, FishButtonImageConfig, \
    FishButtonTextConfig, FishButtonTextBorderConfig, CoinsButtonConfig, CoinsButtonImageConfig, CoinsButtonTextConfig, \
    CoinsButtonTextBorderConfig, HatcheryButtonConfig, HatcheryButtonImageConfig, HatcheryButtonTextConfig, \
    HatcheryButtonTextBorderConfig, DragonsButtonConfig, DragonsButtonImageConfig, DragonsButtonTextConfig, \
    DragonsButtonTextBorderConfig, IslandsButtonConfig, IslandsButtonImageConfig, IslandsButtonTextConfig, \
    IslandsButtonTextBorderConfig, MarketButtonConfig, MarketButtonImageConfig, MarketButtonTextConfig, \
    MarketButtonTextBorderConfig, SettingsButtonConfig, SettingsButtonImageConfig, SettingsButtonTextConfig, \
    SettingsButtonTextBorderConfig

_background = Image(BackgroundConfig())

_trophies_button = Button(TrophiesButtonConfig())
_trophies_button_image = _trophies_button.add_image(TrophiesButtonImageConfig())
_trophies_button_text = _trophies_button.add_text(TrophiesButtonTextConfig(), TrophiesButtonTextBorderConfig())

_eggs_button = Button(EggsButtonConfig())
_eggs_button_image = _eggs_button.add_image(EggsButtonImageConfig())
_eggs_button_text = _eggs_button.add_text(EggsButtonTextConfig(), EggsButtonTextBorderConfig())

_fish_button = Button(FishButtonConfig())
_fish_button_image = _fish_button.add_image(FishButtonImageConfig())
_fish_button_text = _fish_button.add_text(FishButtonTextConfig(), FishButtonTextBorderConfig())

_coins_button = Button(CoinsButtonConfig())
_coins_button_image = _coins_button.add_image(CoinsButtonImageConfig())
_coins_button_text = _coins_button.add_text(CoinsButtonTextConfig(), CoinsButtonTextBorderConfig())

_hatchery_button = Button(HatcheryButtonConfig())
_hatchery_button_image = _hatchery_button.add_image(HatcheryButtonImageConfig())
_hatchery_button_text = _hatchery_button.add_text(HatcheryButtonTextConfig(), HatcheryButtonTextBorderConfig())

_dragons_button = Button(DragonsButtonConfig())
_dragons_button_image = _dragons_button.add_image(DragonsButtonImageConfig())
_dragons_button_text = _dragons_button.add_text(DragonsButtonTextConfig(), DragonsButtonTextBorderConfig())

_islands_button = Button(IslandsButtonConfig())
_islands_button_image = _islands_button.add_image(IslandsButtonImageConfig())
_islands_button_text = _islands_button.add_text(IslandsButtonTextConfig(), IslandsButtonTextBorderConfig())

_market_button = Button(MarketButtonConfig())
_market_button_image = _market_button.add_image(MarketButtonImageConfig())
_market_button_text = _market_button.add_text(MarketButtonTextConfig(), MarketButtonTextBorderConfig())

_settings_button = Button(SettingsButtonConfig())
_settings_button_image = _settings_button.add_image(SettingsButtonImageConfig())
_settings_button_text = _settings_button.add_text(SettingsButtonTextConfig(), SettingsButtonTextBorderConfig())

_easy_level_button = Button(Island1EasyLevelButtonConfig())
_medium_level_button = Button(Island1MediumLevelButtonConfig())
_hard_level_button = Button(Island1HardLevelButtonConfig())
_fiendish_level_button = Button(Island1FiendishLevelButtonConfig())

main_menu_elements = pygame.sprite.Group(_background, _trophies_button, _trophies_button_image, _trophies_button_text,
                                         _eggs_button, _eggs_button_image, _eggs_button_text, _fish_button,
                                         _fish_button_image, _fish_button_text, _coins_button, _coins_button_image,
                                         _coins_button_text, _hatchery_button, _hatchery_button_image,
                                         _hatchery_button_text, _dragons_button, _dragons_button_image,
                                         _dragons_button_text, _islands_button, _islands_button_image,
                                         _islands_button_text, _market_button, _market_button_image,
                                         _market_button_text, _settings_button, _settings_button_image,
                                         _settings_button_text, _easy_level_button, _medium_level_button,
                                         _hard_level_button, _fiendish_level_button)
