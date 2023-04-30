#!/bin/bash
openssl enc -d -des3 -base64 -pbkdf2 -in textocifrado.txt -out $1