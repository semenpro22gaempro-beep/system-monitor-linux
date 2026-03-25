from setuptools import setup

setup(
    name="my-cool-monitor",
    version="1.0",
    py_modules=["monitor"], # имя твоего .py файла без расширения
    install_requires=["psutil", "rich"],
    entry_points={
        "console_scripts": [
            "monitor=monitor:main", # команда "monitor" вызовет функцию main()
        ],
    },
)
