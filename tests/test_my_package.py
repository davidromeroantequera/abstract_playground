from my_package import MyBaseClass, MyCompliantClass, MyNonCompliantClass, MyDerivedClass, MyStillIncorrectDerivedClass
from abstract_checker import check_unimplemented_abstract_methods


def test_my_compliant_class_derives_from_my_base_class():
    assert issubclass(MyCompliantClass, MyBaseClass)


def test_my_compliant_class_implements_my_prop():
    assert hasattr(MyCompliantClass, "my_prop")
    assert callable(MyCompliantClass.my_prop)
    assert not hasattr(MyCompliantClass.my_prop, "__isabstractmethod__")


def test_my_non_compliant_class_derives_from_my_base_class():
    assert issubclass(MyNonCompliantClass, MyBaseClass)


def test_my_non_compliant_class_do_not_implement_my_prop():
    assert hasattr(MyNonCompliantClass, "my_prop")
    assert callable(MyNonCompliantClass)
    assert hasattr(MyNonCompliantClass.my_prop, "__isabstractmethod__")


def test_my_derived_class_implements_my_prop():
    assert hasattr(MyDerivedClass, "my_prop")
    assert callable(MyDerivedClass)
    assert not hasattr(MyDerivedClass.my_prop, "__isabstractmethod__")


def test_my_still_incorrect_derived_class_do_not_implement_my_prop():
    assert hasattr(MyStillIncorrectDerivedClass, "my_prop")
    assert callable(MyStillIncorrectDerivedClass)
    assert hasattr(MyStillIncorrectDerivedClass.my_prop, "__isabstractmethod__")


def test_abstract_checker():
    offending_classes = ['MyBaseClass', 'MyNonCompliantClass', 'MyStillIncorrectDerivedClass']
    assert check_unimplemented_abstract_methods("my_package", "my_prop") == offending_classes
