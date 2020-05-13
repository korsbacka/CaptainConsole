from django.db import models

from consoles.models import Console


class GameGenre(models.Model):
    game_genre_name = models.CharField(max_length=255)
    game_genre_image = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.game_genre_name


class GamePublisher(models.Model):
    game_publisher_name = models.CharField(max_length=255)
    game_publisher_description = models.CharField(max_length=999)
    game_publisher_logo = models.CharField(max_length=999, blank=True)

    def __str__(self):
        return self.game_publisher_name


class Game(models.Model):
    game_name = models.CharField(max_length=255)
    game_genre = models.ForeignKey(GameGenre, on_delete=models.CASCADE)
    game_publisher = models.ForeignKey(GamePublisher, on_delete=models.CASCADE)
    game_short_description = models.CharField(max_length=255)
    game_long_description = models.CharField(max_length=999)
    game_price = models.FloatField()

    def __str__(self):
        return self.game_name


class GameImage(models.Model):
    game_image_image = models.CharField(max_length=999)
    game_image_game = models.ForeignKey(Game, on_delete=models.CASCADE)
