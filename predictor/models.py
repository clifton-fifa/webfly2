from django.db import models

class FamilyModel(models.Model):
    # ตัวอย่างฟิลด์ที่อาจใช้ในโมเดลนี้
    # โปรดปรับเปลี่ยนตามความต้องการของคุณ
    family_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.family_name

class SpeciesModel(models.Model):
    # ตัวอย่างฟิลด์ที่อาจใช้ในโมเดลนี้
    # โปรดปรับเปลี่ยนตามความต้องการของคุณ
    species_name = models.CharField(max_length=255)
    family = models.ForeignKey(FamilyModel, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.species_name
