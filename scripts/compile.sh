#!/bin/bash

if [[ "$PWD" == */scripts ]]; then
  cd ..
fi

echo $PWD

python -m build --wheel
