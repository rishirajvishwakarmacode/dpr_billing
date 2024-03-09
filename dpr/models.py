from django.db import models
from decimal import Decimal


class ExpressionDecimalField(models.DecimalField):
    def to_python(self, value):
        if isinstance(value, Decimal):
            return value
        try:
            return eval(str(value), {}, {})
        except (SyntaxError, NameError, TypeError):
            return None

# Create your models here.
class cabletray(models.Model):

    tray_choice = {
        ("MST", "MST"),
        ("BST", "BST"),
        ("MPT", "MPT"),
        ("BPT", "BPT")
    }

    size_choice = {
        (50, 50),
        (100, 100),
        (150, 150),
        (300, 300),
        (450, 450),
        (600,600)
    }

    date_added = models.DateField(auto_now_add=True)
    unit = models.CharField(max_length=50, choices = {("111","111"), ("515", "515")}, default = "111")
    id = models.CharField(max_length=50, unique=True, primary_key=True, blank=True)
    tag = models.CharField(max_length=50)
    tray_type = models.CharField(choices=tray_choice, max_length=3)
    size = models.DecimalField(choices=size_choice, max_digits=5, decimal_places=0)
    from_col = models.CharField(max_length=100, blank=True)
    to_col = models.CharField(max_length=100, blank=True)
    from_ele = models.CharField(max_length=100, blank=True)
    to_ele = models.CharField(max_length=100, blank=True)
    length_completed = models.DecimalField(decimal_places=2, max_digits=5, default=0.00)
    area = models.CharField(max_length=8)
    tray_size_code = models.CharField(max_length = 2, blank=True)
    ISMC_100 = models.DecimalField(max_digits=10, decimal_places=5, default=0.00000)
    ISA_50 = models.DecimalField(max_digits=10, decimal_places=5, default=0.00000)
    ISA_40 = models.DecimalField(max_digits=10, decimal_places=5, default=0.00000)

    def save(self, *args, **kwargs):
        if not self.tray_size_code:
            if self.size == 50:
                self.tray_size_code = "A"
            elif self.size==100:
                self.tray_size_code = "B"
            elif self.size==150:
                self.tray_size_code = "C"
            elif self.size==300:
                self.tray_size_code = "E"
            elif self.size==450:
                self.tray_size_code = "G"
            elif self.size==600:
                self.tray_size_code = "H"


        if not self.id:  # Generate ID if it doesn't exist
            self.id = f"{self.unit}-{self.tray_type}-{self.tag}-{self.tray_size_code}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.id

