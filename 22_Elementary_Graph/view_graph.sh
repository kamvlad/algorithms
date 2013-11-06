#!/bin/bash

name=${1%.*}
dot -Kcirco $1 -Tpng -o $name.png && gthumb $name.png
