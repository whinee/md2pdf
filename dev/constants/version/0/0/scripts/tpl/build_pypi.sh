#!/usr/bin/env bash
just bootstrap &&
source pyenv/bin/activate &&
poetry build