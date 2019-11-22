#!/usr/bin/env python3
#
# Demonstrate getting asset information
#
#
#web3fusion
from  web3fsnpy import Fsn

linkToChain = {
    'network'     : 'testnet',     # One of 'testnet', or 'mainnet'
    'provider'    : 'WebSocket',   # One of 'WebSocket', 'HTTP', or 'IPC'
    'gateway'     : 'default',
}

web3fsn = Fsn(linkToChain)
#
#
#asset_name = 'FSN'
asset_name = 'TST5'
blockNo = 'latest'
#
#
asset_Id = web3fsn.getAssetId(asset_name)
print('asset_Id = ',asset_Id)
#
if asset_Id != None:
    asset_dict = web3fsn.getAsset(asset_Id,blockNo)
#
#   print(asset_dict,'\n')
#
#
    for key, Id in asset_dict.items():
        print(key, ' :    ', Id)

