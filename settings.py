import os.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_DIR = os.path.join(BASE_DIR, "audio")
HIT = os.path.join(AUDIO_DIR, "hit.wav")
PONG = os.path.join(AUDIO_DIR, "pong.wav")
DEAD = os.path.join(AUDIO_DIR, "no.wav")
OOF = os.path.join(AUDIO_DIR, "oof.wav")
DOH = os.path.join(AUDIO_DIR, "doh.wav")
BRUH = os.path.join(AUDIO_DIR, "bruh.wav")
MIF = os.path.join(AUDIO_DIR, "mif.wav")
BULLY = os.path.join(AUDIO_DIR, "bully.wav")
CJ = os.path.join(AUDIO_DIR, "cj.wav")

BALLLEAVING = 0
# Color enumerators.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (78, 255, 87)
YELLOW = (241, 255, 0)
BLUE = (80, 255, 239)
PURPLE = (203, 0, 255)
RED = (237, 28, 36)
COLOR = RED
COUNTER = 0
#self.velocity[1] min,max
BALLSPEED1 = -14.00
BALLSPEED2 = 14.00
# Wall borders where the ball will bounce.
TOP_WALL = 0
BOTTOM_WALL = 690
LEFT_WALL = 0
RIGHT_WALL = 690
#DEBUG AND BOTS!
DEBUG = False
BOTS = False
AUDIO = False

BALL_SPRITE = {
    "file": "ballxd.png",
    "size": [10, 10],
}