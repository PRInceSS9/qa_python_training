# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
def test_add_new_contact(app):
    app.open_main_page()
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Василий", middlename="Анатольевич", lastname="Кусков", bday="9",
                               bmonth="November", byear="1998"))

    