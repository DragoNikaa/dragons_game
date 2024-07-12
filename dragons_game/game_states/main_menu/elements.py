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

_trophies_button = Button(TrophiesButtonConfig(), image_config=TrophiesButtonImageConfig(),
                          text_config=TrophiesButtonTextConfig(), text_border_config=TrophiesButtonTextBorderConfig())
_eggs_button = Button(EggsButtonConfig(), image_config=EggsButtonImageConfig(), text_config=EggsButtonTextConfig(),
                      text_border_config=EggsButtonTextBorderConfig())
_fish_button = Button(FishButtonConfig(), image_config=FishButtonImageConfig(), text_config=FishButtonTextConfig(),
                      text_border_config=FishButtonTextBorderConfig())
_coins_button = Button(CoinsButtonConfig(), image_config=CoinsButtonImageConfig(), text_config=CoinsButtonTextConfig(),
                       text_border_config=CoinsButtonTextBorderConfig())

_hatchery_button = Button(HatcheryButtonConfig(), image_config=HatcheryButtonImageConfig(),
                          text_config=HatcheryButtonTextConfig(), text_border_config=HatcheryButtonTextBorderConfig())
_dragons_button = Button(DragonsButtonConfig(), image_config=DragonsButtonImageConfig(),
                         text_config=DragonsButtonTextConfig(), text_border_config=DragonsButtonTextBorderConfig())
_islands_button = Button(IslandsButtonConfig(), image_config=IslandsButtonImageConfig(),
                         text_config=IslandsButtonTextConfig(), text_border_config=IslandsButtonTextBorderConfig())
_market_button = Button(MarketButtonConfig(), image_config=MarketButtonImageConfig(),
                        text_config=MarketButtonTextConfig(), text_border_config=MarketButtonTextBorderConfig())
_settings_button = Button(SettingsButtonConfig(), image_config=SettingsButtonImageConfig(),
                          text_config=SettingsButtonTextConfig(), text_border_config=SettingsButtonTextBorderConfig())

_easy_level_button = Button(Island1EasyLevelButtonConfig())
_medium_level_button = Button(Island1MediumLevelButtonConfig())
_hard_level_button = Button(Island1HardLevelButtonConfig())
_fiendish_level_button = Button(Island1FiendishLevelButtonConfig())

main_menu_elements = pygame.sprite.Group(_background, _trophies_button, _eggs_button, _fish_button, _coins_button,
                                         _hatchery_button, _dragons_button, _islands_button, _market_button,
                                         _settings_button, _easy_level_button, _medium_level_button, _hard_level_button,
                                         _fiendish_level_button)
