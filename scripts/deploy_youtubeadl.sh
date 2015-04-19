#!/bin/bash

cd ../ansible

#ansible-playbook -i production ../ansible/site.yml --tags="deploy,celery" --ask-vault-pass -vvvv
ansible-playbook -i production ../ansible/site.yml --ask-vault-pass
