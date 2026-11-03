#!/bin/bash

if [[ "$PWD" == */scripts ]]; then
  cd ..
fi

echo $PWD

python3.15 -m venv ./.venv
source ./.venv/bin/activate
python -m pip install -e ".[dev]"
