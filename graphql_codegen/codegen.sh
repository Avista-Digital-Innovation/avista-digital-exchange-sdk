#!/bin/bash

echo ""
echo "Step 1 of 4 - Moving to gqlg dir"
cd ./step_1_gqlg

echo ""
echo "Step 2 of 4 - Running ./step_1_gqlg/generate.sh"
./generate.sh

echo ""
echo "Step 3 of 4 - Moving to ariadne dir"
cd ../step_2_ariadne

echo ""
echo "Step 4 of 4 - Running ./step_2_ariadne/generate.sh"
./generate.sh

echo "Done"