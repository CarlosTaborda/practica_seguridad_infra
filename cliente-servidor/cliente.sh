#!/bin/bash
openssl enc -e -des3 -base64 -pbkdf2 -in $1 -out textocifrado.txt
rm $1