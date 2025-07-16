#!/bin/bash
echo "Test scan JSON structure"
jq . scan-results/helloworld-*.json | head -n 20
