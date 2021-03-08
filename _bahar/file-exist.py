import os

dosya_yolu = "C:\_DERS_ORNEKLER\PYTHON\_bahar\deneme.txt"


if os.path.exists(dosya_yolu):
  os.remove(dosya_yolu)
else:
  print("Zaten böyle bir dosya yok!")