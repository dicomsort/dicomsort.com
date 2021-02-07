from setuptools import Command, setup


class FreezeCommand(Command):
    """Freeze the flask application into static files."""
    description = 'Freeze the flask application'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from flask_frozen import Freezer
        from app import app

        freezer = Freezer(app)
        freezer.freeze()


setup(
    name='dicomsort.com',
    cmdclass={
        'freeze': FreezeCommand
    }
)
