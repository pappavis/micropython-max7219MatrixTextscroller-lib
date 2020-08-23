# micropython-max7219MatrixTextscroller-lib
A text scroller extension library for Micropython


# voorbeeld gebruik:
```python
from Max7219Textscroller import MatrixTextscroller


def init():
    scoller1 = MatrixTextscroller()
    scoller1.debug = False
    scoller1.scrollText(textToScroll='    Hallo1239809876543210')


print('App start')
init()
print('App eind')
```
