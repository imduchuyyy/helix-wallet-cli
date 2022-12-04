# Mini Cool Wallet - MCWallet
MCWallet is python script encrypt your private key. Unlike normal extension wallet, MCWallet can't connect to browser, so it can't be hack

![alt text](./assets/preview.jpg)

## Set up
1. Install package
```sh
pip3 install -r requirements.txt

```
or 
```sh
pipenv sync
```

2. Execute mod for wallet.py
```sh
chmod 777 ./wallet.py
```

## Usage
1. Run app
```sh
./wallet.py
```
NOTE:
By default, we use RPC from infura service to get balance and transaction. If you want to use your own node, you can change config file
```shell
config set --url "https://mainnet.infura.io/v3/your_api_key" --keypair-file "path/to/your/keypair/file"
```

If you not have wallet, it will create new wallet and save to file *.json by command
```sh
 create --force
```
You can change url and keypair_path for your own config in `~/.tartarus-wallet/config.json` and view your wallet keypair in `~/tartarus-wallet/wallet/id.json`

2. Get wallet address
```sh
>> address
```

3. Transfer Token
```sh
>> transfer
```

4. Reset wallet
```sh
>> reset
```

## Test 
1. Run test 
```sh 
pytest -s
```

or 
```sh
./quicktest.sh
```

## TODO
1. Support tornado cash
2. Refactor code

## Thanks for use
Donate ♥  <b>0x094C569ed04f3d93Ac8656e5cf2522381E24D57D</b>
