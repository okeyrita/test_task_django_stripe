from django.db import models
from django.urls import reverse


class Item(models.Model):
    '''
    Model for representing a product item.
    '''
    name = models.CharField(
        max_length=100,
        help_text='Enter a name of product.'
    )

    description = models.TextField(
        max_length=200,
        help_text='Enter a description of product.')

    price = models.PositiveIntegerField(
        help_text='Enter a price of product.'
    )

    def get_absolute_url(self):
        '''Returns the url to particular item.'''
        return reverse('item', args=[str(self.id)])

    def get_buy_url(self):
        '''Returns the url with session id to buy item '''
        return reverse('buy_item', args=[str(self.id)])

    def __str__(self):
        '''String for representing the Item object.'''
        return self.name
