import os
from detection import run_detection

pictures = [picture for picture in os.listdir('./pictures')]
for picture in pictures:
    run_detection(picture)
