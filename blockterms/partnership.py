from blockterms.storage import StorageAPI
from boa.code.builtins import range, concat
from boa.blockchain.vm.Neo.Runtime import Log, Notify


class Partnership(object):

    def create_partnership(self,address,currency,flatfees_struc,partnership_struc,webpage):
        """
            address, currency, flatfees_struc, partnership_struc, webpage
            Creates the partnership structure for the given address
            format for flatfee_struc = addr:fees,addr:fees...
            format for partnership_struc = addr:fees,addr:fees...
            :return: indication success execution of the command
            :rtype: bool
        """
        storage = StorageAPI()
        terms = [currency, flatfees_struc, partnership_struc, webpage]
        serterms = storage.serialize_array(terms)
        storage.put(address, serterms)
        msg = concat("New Partnership Created:", " ")
        a = concat("Address : ", address)
        msg = concat(msg, a)
        c = concat(", Currency : ", currency)
        msg = concat(msg, c)
        d = concat(", Flatfee Structure : ", flatfees_struc)
        msg = concat(msg, d)
        e = concat(", Partnership Structure: ", partnership_struc)
        msg = concat(msg, e)
        f = concat(", Webpage: ", webpage)
        msg = concat(msg, f)
        Notify(msg)
        return True

    def print_info(self,address):
        """
            Prints the information stored in the blockchain for the given address
            :return: indication success execution of the command
            :rtype: bool
        """
        storage = StorageAPI()
        termsba = storage.get(address)
        if not termsba:
            Notify("Partnership for address is not yet created")
            return False

        serterms = storage.deserialize_bytearray(termsba)
        currency = serterms[0]
        flatfees_struc = serterms[1]
        partnership_struc = serterms[2]
        webpage = serterms[3]
        msg = concat("Partnership Information:", " ")
        a = concat("Address : ", address)
        msg = concat(msg, a)
        c = concat(", Currency : ", currency)
        msg = concat(msg, c)
        d = concat(", Flatfee Structure : ", flatfees_struc)
        msg = concat(msg, d)
        e = concat(", Partnership Structure: ", partnership_struc)
        msg = concat(msg, e)
        f = concat(", Webpage: ", webpage)
        msg = concat(msg, f)
        Notify(msg)
        return True

    def delete(self, address):
        msg = concat("Delete Partnership: ", address)
        Notify(msg)

        storage = StorageAPI()
        termsba = storage.get(address)
        if not termsba:
            Notify("Partnership for address is not yet created")
            return False
        storage.delete(address)
        return True

    def transfer(self, from_address, to_address):
        frm = concat("From ", from_address)
        to = concat("To ", to_address)
        msg = concat("Transfer Partnership: ", frm)
        msg = concat(msg, to)
        Notify(msg)

        storage = StorageAPI()
        termsba = storage.get(from_address)
        if not termsba:
            Notify("Partnership for address is not yet created")
            return False
        storage.put(to_address,termsba)
        storage.delete(from_address)
        return True

    def set_partnership(self, address, partnership_struc):
        msg = concat("Change partnership structure for: ", address)
        Notify(msg)

        storage = StorageAPI()
        termsba = storage.get(address)
        if not termsba:
            Notify("Partnership for address is not yet created")
            return False
        serterms = storage.deserialize_bytearray(termsba)
        currency = serterms[0]
        flatfees_struc = serterms[1]
        webpage = serterms[3]

        terms = [currency, flatfees_struc, partnership_struc, webpage]
        serterms = storage.serialize_array(terms)
        storage.put(address, serterms)

        msg = concat("Partnership updated:", " ")
        a = concat("Address : ", address)
        msg = concat(msg, a)
        c = concat(", Currency : ", currency)
        msg = concat(msg, c)
        d = concat(", Flatfee Structure : ", flatfees_struc)
        msg = concat(msg, d)
        e = concat(", Partnership Structure: ", partnership_struc)
        msg = concat(msg, e)
        f = concat(", Webpage: ", webpage)
        msg = concat(msg, f)
        Notify(msg)
        return True

    def set_flatfees(self, address, flatfees_struc):
        msg = concat("Change flatfees structure for: ", address)
        Notify(msg)

        storage = StorageAPI()
        termsba = storage.get(address)
        if not termsba:
            Notify("Partnership for address is not yet created")
            return False
        serterms = storage.deserialize_bytearray(termsba)
        currency = serterms[0]
        partnership_struc = serterms[2]
        webpage = serterms[3]

        terms = [currency, flatfees_struc, partnership_struc, webpage]
        serterms = storage.serialize_array(terms)
        storage.put(address, serterms)

        msg = concat("Partnership updated:", " ")
        a = concat("Address : ", address)
        msg = concat(msg, a)
        c = concat(", Currency : ", currency)
        msg = concat(msg, c)
        d = concat(", Flatfee Structure : ", flatfees_struc)
        msg = concat(msg, d)
        e = concat(", Partnership Structure: ", partnership_struc)
        msg = concat(msg, e)
        f = concat(", Webpage: ", webpage)
        msg = concat(msg, f)
        Notify(msg)
        return True

    def set_webpage(self, address, webpage):
        msg = concat("Change webpage for: ", address)
        Notify(msg)
        storage = StorageAPI()
        termsba = storage.get(address)
        if not termsba:
            Notify("Partnership for address is not yet created")
            return False
        serterms = storage.deserialize_bytearray(termsba)
        currency = serterms[0]
        flatfees_struc = serterms[1]
        partnership_struc = serterms[2]

        msg = concat("Webpage updated:", " ")
        a = concat("Address : ", address)
        msg = concat(msg, a)
        c = concat(", Currency : ", currency)
        msg = concat(msg, c)
        d = concat(", Flatfee Structure : ", flatfees_struc)
        msg = concat(msg, d)
        e = concat(", Partnership Structure: ", partnership_struc)
        msg = concat(msg, e)
        f = concat(", Webpage: ", webpage)
        msg = concat(msg, f)
        Notify(msg)
        return True
