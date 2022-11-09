from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Game(models.Model):
    TITLE_MAX_LEN = 30

    CATEGORY_MAX_LEN = 15

    ACTION = "Action"
    ADVENTURE = "Adventure"
    PUZZLE = "Puzzle"
    STRATEGY = "Strategy"
    SPORTS = "Sports"
    BOARD_CARD_GAME = "Board/Card Game"
    OTHER = "Other"
    CATEGORIES = ((x, x) for x in (ACTION, ADVENTURE, PUZZLE, STRATEGY,
                                   SPORTS, BOARD_CARD_GAME, OTHER))

    RATING_MIN_VALUE = 0.1
    RATING_MAX_VALUE = 5.0

    MAX_LEVEL_MIN_VALUE = 1

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        unique=True,
    )

    category = models.CharField(
        max_length=CATEGORY_MAX_LEN,
        choices=CATEGORIES,
    )

    rating = models.FloatField(
        validators=(
            MinValueValidator(RATING_MIN_VALUE),
            MaxValueValidator(RATING_MAX_VALUE),
        )
    )

    max_level = models.IntegerField(
        validators=(
            MinValueValidator(MAX_LEVEL_MIN_VALUE),
        )
    )

    image_url = models.URLField(
        verbose_name='Image URL',
    )

    summary = models.TextField(
        null=True,
        blank=True,
    )