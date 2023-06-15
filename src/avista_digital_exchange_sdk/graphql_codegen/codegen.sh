#!/bin/bash

echo ""
echo "Step 1 of 4 - Moving to gqlg dir"
cd ./gqlg

echo ""
echo "Step 2 of 4 - Running ./gqlg/generate.sh"
./generate.sh

echo ""
echo "Step 3 of 4 - Moving to ariadne dir"
cd ../ariadne

echo ""
echo "Step 4 of 4 - Running ./ariadne/generate.sh"
./generate.sh

echo "Done"