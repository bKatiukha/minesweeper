from unittest import mock
import matplotlib.pyplot as plt
from PIL import Image
from src.draw_shapes.draw_shapes import draw_circle, draw_rectangle


def test_draw_circle():
    """Test for draw_circle function"""

    with mock.patch.object(plt, 'show') as mock_show:
        draw_circle()
        mock_show.assert_called_once()


def test_draw_rectangle():
    """Test for draw_rectangle function"""

    with mock.patch.object(Image.Image, 'show') as mock_show:
        draw_rectangle()
        mock_show.assert_called_once()
