import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'C1\xc4\xea\xb5\x13\xed\xce\x05\x87\x1d\xdbJ\x00\x15d\xec||3\x8e\xd0V'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'karczma.db')