
run:
  python3 -m biliass

release:
  python3 setup.py upload
  just clean-builds

upgrade-pip:
  python3 -m pip install --upgrade biliass

upgrade:
  python3 setup.py build
  python3 setup.py install

clean:
  find . -name "*.xml" -print0 | xargs -0 rm -f
  find . -name "*.ass" -print0 | xargs -0 rm -f

clean-builds:
  rm biliass/py.typed
  rm -rf biliass/biliass.pyi
  rm -rf .mypy_cache/
  rm -rf **/__pycache__
  rm -rf biliass.egg-info/
  rm -rf build/
  rm -rf dist/
