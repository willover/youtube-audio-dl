#!/bin/bash

cd ../ansible

ansible-playbook -i production ../ansible/site.yml --ask-vault-pass
