#!/bin/bash

cd ../ansible

ansible-playbook -i production ../ansible/site.yml --tags="deploy,nginx,virtualenv" --ask-vault-pass
#ansible-playbook -i production ../ansible/site.yml --ask-vault-pass
