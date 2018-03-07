## blockterms Partnership contracts for neo blockchain

### Introduction

  What are partnership contracts? 
  
  In everyday economy, multiple parties come together to provide a product or service. 
  When a consumer pays for that product or service, all that collaboration information 
  is not so easy to find out. There is no transparency for who is getting what part of 
  the consumer payment.
  
  Some examples of partnerships are 
  
1. Uber/ridesharing service + driver is a partnership 
2. Expedia/Hotel Booking + Hotel owner is a partnership
3. Amazon + Retailer + Manufacturer is also form a partnership
  
  When a consumer makes a transaction, all the partners eventually get paid but the information is not so 
  transparent and settlement of funds takes time and it needs a lot of trust. This is due to limitations on 
  the existing financial institutions.
  
  blockterms leverages blockchain, digital currencies and computer algorithms to show how multiple parties can 
  come together and create a ownership structure on public blockchain behind a Digital currency address to 
  provide pricing and ownership transparency.
  
  There are two important parts for this system.
  
  1. Ownership structure behind an address. This is stored on blockchain. This code is the implementation for 
  the same.
  2. Settlement Algorithms. These are not part of this repo.
  
  When a payment transaction happens on the partnership address, Settlement algorithms of blockterms ensures all 
  the parties get their share of the ownership according to the terms of the partnership.
  
  This reference implementation, stores only two kinds of simple partnerships. The flat fees and percentage based
  partnership.
  
  
### Setup
If you are new to neo smart contracts or how to get started with neo blockchain using python review these links.

http://docs.neo.org/en-us/index.html

https://github.com/CityOfZion/python-smart-contract-workshop

https://github.com/CityOfZion/neo-python



   
### Data Stored on the blockchain.

```
This the data needed for a partnership contract.
1. Address where the payment is accepted
2. Currency of the Contract
3. FlatFeestructure addr:val,addr:val......
4. PartnershipStructure addr:val,addr:val......
5. A Website Address where users can find more information
```

### Methods inside the Partnership Smart Contract

1. create - Adds the partnership data to the blcokchain. Key is the Address and the value is described above.
2. info - provides partnership information for a given address
3. delete - Deletes the partnership information for the address
4. transfer - treansfers the ownership from address A to address B
5. set_webpage - updates the webpage for the given partnership
6. set_flatfees - updates the flatfees structure for a given address
7. set_partnership - updates the percentage ownership structure for a given address.

There is a corresponding method in blockterms/partnership.py file.

```
Methods on Partnership.py
    1. create_partnership(address, currency,
                         FlatFeestructure[], 
                         PartnershipStructure[], webpage)
    2. transfer(fromAddress, toAddress)
    3. delete(address) -- all the funds to the address will be routed to contract address.
    4. set_flatfees(address, ffstruct)
    5. set_partnership(address,PartnershipStructure)
    6. set_webpage(address,webpage)
    7. print_info(address)
```


##How To run the methods in the contract?

###Create
``` 
build ../blocktermsNeoContracts/partnership_contract.py test 0710 01 True False create ["addr1","GAS","ad1:1.23,ad22:4.56","addr1:50.00,addr2:50.00","https://blockterms.com/helloworld"]
```
### Update Flatfees
```
build ../blocktermsNeoContracts/partnership_contract.py test 0710 01 True False set_flatfees ["addr1","addr1:1234"]
```

### Update Webpage
```
build ../blocktermsNeoContracts/partnership_contract.py test 0710 01 True False set_webpage ["addr1","https://a.com"] 
```

### Update Percentage Partnership
```
build ../blocktermsNeoContracts/partnership_contract.py test 0710 01 True False set_partnership ["addr1","addr1:51,addr2:49"]
```

### Delete a Partnership Address
```
build ../blocktermsNeoContracts/partnership_contract.py test 0710 01 True False delete ["addr1"]
```

### Get information
```
build ../blocktermsNeoContracts/partnership_contract.py test 0710 01 True False info ["addr1"]
```

### Transfer Partnership Address
```
build ../blocktermsNeoContracts/partnership_contract.py test 0710 01 True False transfer ["addr1","addr2]
```

If you want to deploy this contract, set correct owner value in partnership_contract.py for testnet/mainnet/privnet


## Links

https://blockterms.com

http://docs.neo.org/en-us/index.html

https://github.com/CityOfZion/python-smart-contract-workshop

https://github.com/CityOfZion/neo-python

https://neo-python.readthedocs.io/en/latest/