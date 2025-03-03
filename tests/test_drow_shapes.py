import pytest
from unittest import mock
import matplotlib.pyplot as plt
import cv2
from PIL import Image
from src.draw_shapes.draw_shapes import draw_circle, draw_rectangle, draw_line


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


def test_draw_line():
    """Test for draw_line function"""

    with mock.patch.object(cv2, 'imshow') as mock_imshow, \
            mock.patch.object(cv2, 'waitKey') as mock_waitkey, \
            mock.patch.object(cv2, 'destroyAllWindows') as mock_destroy:
        draw_line()

        mock_imshow.assert_called_once_with('Line',
                                            mock.ANY)

        mock_waitkey.assert_called_once_with(0)
        mock_destroy.assert_called_once()
