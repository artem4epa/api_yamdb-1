from django.db import models

# Create your models here.


class Review(models.Model):
    title = models.ForeignKey(
        'Title',
        on_delete=models.CASCADE,
        related_name='reviews',
        help_text='введите произведения',
        verbose_name='Произведения',
    )
    text = models.TextField(
        help_text='введите текст отзыва',
        verbose_name='текст отзыва')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        help_text='введите дату публикации ',
        verbose_name='дата публикации')
    author = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='reviews',
        help_text='введите автора',
        verbose_name='Автор',
    )
    score = models.IntegerField(
        help_text='укажите оценку произведения',
        verbose_name='оценка',
    )


class Comment(models.Model):
    review = models.ForeignKey(
        'Review',
        on_delete=models.CASCADE,
        related_name='comments',
        help_text='введите отзыв',
        verbose_name='Отзыв',
    )
    text = models.TextField(
        help_text='введите текст комментария',
        verbose_name='текст комментария')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        help_text='введите дату публикации ',
        verbose_name='дата публикации')
    author = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='reviews',
        help_text='введите автора',
        verbose_name='Автор',
    )
