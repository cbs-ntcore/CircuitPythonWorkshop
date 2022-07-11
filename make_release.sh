#!/bin/bash

VER=`git describe --tags --abbrev=0`
FN="CircuitPythonWorkshop.$VER.zip"

pushd release
zip ../$FN -r ./
popd
