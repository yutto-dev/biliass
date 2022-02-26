
run:
  python3 -m biliass

publish:
  python3 setup.py upload
  just clean-builds

test:
  just gen-test-files
  pytest
  just clean

upgrade-pip:
  python3 -m pip install --upgrade --pre biliass

upgrade:
  python3 setup.py build
  python3 setup.py install

clean:
  find . -name "*.xml" -print0 | xargs -0 rm -f
  find . -name "*.ass" -print0 | xargs -0 rm -f
  find . -name "*.pb" -print0 | xargs -0 rm -f
  find . -name "*.m4s" -print0 | xargs -0 rm -f
  find . -name "*.mp4" -print0 | xargs -0 rm -f
  find . -name "*.aac" -print0 | xargs -0 rm -f
  find . -name "*.xml" -print0 | xargs -0 rm -f
  find . -name "*.srt" -print0 | xargs -0 rm -f
  find . -name "*.ass" -print0 | xargs -0 rm -f
  rm -rf .pytest_cache

clean-builds:
  rm biliass/py.typed
  rm -rf biliass/biliass.pyi
  rm -rf .mypy_cache/
  rm -rf **/__pycache__
  rm -rf biliass.egg-info/
  rm -rf build/
  rm -rf dist/

compile-protobuf:
  protoc --python_out=biliass protobuf/danmaku.proto

gen-test-files:
  python3 scripts/gen_test_files.py