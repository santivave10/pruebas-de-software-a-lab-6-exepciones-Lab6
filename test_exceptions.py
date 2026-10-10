import pytest
from Exceptions import ExceptionsDemo, MyException  

@pytest.mark.unit
def test_divide_zero():
    demo = ExceptionsDemo()
    with pytest.raises(ZeroDivisionError):
        demo.divide(10,0)

@pytest.mark.unit
def test_type_error():
    demo = ExceptionsDemo()
    with pytest.raises(TypeError):
        demo.divide(10,"hola")

@pytest.mark.unit
def test_type_error():
    demo = ExceptionsDemo()
    with pytest.raises(KeyError):
        demo.access_list([3,5,4],7)

@pytest.mark.unit
def test_index_error():
    demo = ExceptionsDemo()
    with pytest.raises((IndexError),(IndexError)):
        demo.access_list([3,5,4],1)
        demo.access_list([3,5,4],7)
        demo.access_list([3,5,4],"5")

@pytest.mark.unit
def test_type_error():
    demo = ExceptionsDemo()
    with pytest.raises(KeyError):
        demo.access_dict({"MANZANA": "DULCE", "LIMON": "AGRIO"}, "TOMATE")

@pytest.mark.unit
def test_FileNotFound_error():
    demo = ExceptionsDemo()
    with pytest.raises(FileNotFoundError):
        demo.read_file("tex.txt")

@pytest.mark.unit
def test_attribute_error():
    demo = ExceptionsDemo()
    demofake = ExceptionsDemo()
    with pytest.raises(AttributeError):
        demo.access_attribute(demofake)

@pytest.mark.wip
def test_myexception_error():
    demo = ExceptionsDemo()
    demofake = ExceptionsDemo()
    with pytest.raises(MyException):
        demo.check_positive(-3)