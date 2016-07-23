#!/bin/bash
VM=$1
VBoxManage showvminfo $VM | grep 'Name:'
VBoxManage showvminfo $VM | grep 'Number of CPUs:'
VBoxManage showvminfo $VM | grep 'Memory size'
VBoxManage showvminfo $VM | grep 'NIC'


