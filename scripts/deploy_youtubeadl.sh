#!/bin/bash

cd ../ansible

ansible-playbook -i production ../ansible/site.yml --tags="deploy" --ask-vault-pass