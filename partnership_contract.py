"""
blockterms simple partnership contract
======================================
Author: Anil Kumar
Email: yak@fastmail.com
Date: Dec 22 2018
"""
from boa.interop.Neo.Runtime import GetTrigger, CheckWitness, Notify
from boa.interop.Neo.TriggerType import Application, Verification
from boa.interop.Neo.Runtime import Notify
from boa.interop.Neo.Storage import Get, Put, Delete, GetContext
from boa.builtins import range, concat, substr

#
# This is the script hash of the address for the owner of the token
# This can be found in ``neo-python`` with the wallet open, use ``wallet`` command
# Use the correct one for private or test or main network
#
OWNER = b'\x07Q\xe9\xe7\x943\x8dAf\x89\x90\xb7\x96\xf8\xbc\xf7\xf1\xca~\xf9'
arg_error = 'Incorrect Arg Length'
ctx = GetContext()

def Main(operation, args):
    """
        :param operation: The name of the operation to perform
        :param args: A list of arguments along with the operation
        :type operation: str
        :type args: list
        :return: The result of the operation
        :rtype: bytearray
        """

    trigger = GetTrigger()
    if trigger == Verification():
        Notify("Verification")
        is_owner = CheckWitness(OWNER)

        if is_owner:
            return True
        else:
            return False

    elif trigger == Application():
        Notify("Application")

        if operation == 'create':
            return do_create(args)
        elif operation == 'transfer':
            return do_transfer(args)
        elif operation == 'info':
            return do_info(args)
        elif operation == 'delete':
            return do_delete_partnership(args)
        elif operation == 'set_partnership':
            return do_set_percentage_partnership(args)
        elif operation == 'set_flatfees':
            return do_set_flatfee_partnership(args)
        elif operation == 'set_webpage':
            return do_set_webpage(args)
        else:
            Notify('unknown operation')
            return False


def do_create(args):
    nargs = len(args)
    is_owner = CheckWitness(OWNER)

    if is_owner:
        if nargs == 5:
            adr = args[0]
            currency = args[1]
            flatfees_struc = args[2]
            partnership_struc = args[3]
            webpage = args[4]
            create_partnership(adr,currency,flatfees_struc,partnership_struc,webpage)
            return True
        Notify(arg_error)
        return False
    else:
        Notify("Unauthorized to create Partnership")
        return False


def do_transfer(args):
    is_owner = CheckWitness(OWNER)

    if is_owner:
        if len(args) == 2:
            from_address = args[0]
            to_address = args[1]
            transfer(from_address,to_address)
            return True
        Notify(arg_error)
        return False
    else:
        Notify("Unauthorized to transfer Partnership")
        return False


def do_info(args):
    nargs = len(args)
    if nargs == 1:
        adr = args[0]
        return print_info(adr)
    Notify(arg_error)
    return []


def do_delete_partnership(args):
    is_owner = CheckWitness(OWNER)

    if is_owner:
        nargs = len(args)
        if nargs == 1:
            adr = args[0]
            delete_partnership(adr)
            return True
        Notify(arg_error)
        return False
    else:
        Notify("Unauthorized to delete Partnership")
        return False


def do_set_percentage_partnership(args):
    is_owner = CheckWitness(OWNER)
    if is_owner:
        nargs = len(args)
        if nargs == 2:
            adr = args[0]
            partnership_struc = args[1]
            set_partnership(adr,partnership_struc)
            return True
        Notify(arg_error)
        return False
    else:
        Notify("Unauthorized to edit Partnership")
        return False


def do_set_flatfee_partnership(args):
    is_owner = CheckWitness(OWNER)
    if is_owner:
        nargs = len(args)
        if nargs == 2:
            adr = args[0]
            flatfee_struc = args[1]
            set_flatfees(adr, flatfee_struc)
            return True
        Notify(arg_error)
        return False
    else:
        Notify("Unauthorized to edit Partnership")
        return False


def do_set_webpage(args):
    is_owner = CheckWitness(OWNER)
    if is_owner:
        nargs = len(args)
        if nargs == 2:
            adr = args[0]
            webpage = args[1]
            set_webpage(adr, webpage)
            return True
        Notify(arg_error)
        return False
    else:
        Notify("Unauthorized to edit Partnership")
        return False


def create_partnership(adr,currency,flatfees_struc,partnership_struc,webpage):
    """
        address, currency, flatfees_struc, partnership_struc, webpage
        Creates the partnership structure for the given address
        format for flatfee_struc = addr:fees,addr:fees...
        format for partnership_struc = addr:fees,addr:fees...
        :return: indication success execution of the command
        :rtype: bool
    """
    terms = [currency, flatfees_struc, partnership_struc, webpage]
    serterms = serialize_array(terms)
    Put(ctx, adr, serterms)
    msg = concat("New Partnership Created:", " ")
    a = concat("Address : ", adr)
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


def print_info(adr):
    """
        Prints the information stored in the blockchain for the given address
        :return: indication success execution of the command
        :rtype: bool
    """
    termsba = Get(ctx,adr)
    if not termsba:
        Notify("Partnership for address is not yet created")
        return False

    serterms = deserialize_bytearray(termsba)
    currency = serterms[0]
    flatfees_struc = serterms[1]
    partnership_struc = serterms[2]
    webpage = serterms[3]
    msg = concat("Partnership Information:", " ")
    a = concat("Address : ", adr)
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

    json_like_string = concat('{ "currency" : "', currency)
    json_like_string = concat(json_like_string, '", "flatfee_partners" : "')
    json_like_string = concat(json_like_string, flatfees_struc)
    json_like_string = concat(json_like_string, '", "percentage_partners" : "')
    json_like_string = concat(json_like_string, partnership_struc)
    json_like_string = concat(json_like_string, '", "webpage" : "')
    json_like_string = concat(json_like_string, webpage)
    json_like_string = concat(json_like_string, '"}')

    return json_like_string


def delete_partnership(adr):
    msg = concat("Delete Partnership: ", adr)
    Notify(msg)

    termsba = Get(ctx,adr)
    if not termsba:
        Notify("Partnership for address is not yet created")
        return False
    Delete(ctx,adr)
    return True


def transfer(from_address, to_address):
    frm = concat("From ", from_address)
    to = concat("To ", to_address)
    msg = concat("Transfer Partnership: ", frm)
    msg = concat(msg, to)
    Notify(msg)

    termsba = Get(ctx,from_address)
    if not termsba:
        Notify("Partnership for address is not yet created")
        return False
    Put(ctx,to_address,termsba)
    Delete(ctx,from_address)
    return True


def set_partnership(adr, partnership_struc):
    msg = concat("Change partnership structure for: ", adr)
    Notify(msg)

    termsba = Get(ctx,adr)
    if not termsba:
        Notify("Partnership for address is not yet created")
        return False
    serterms = deserialize_bytearray(termsba)
    currency = serterms[0]
    flatfees_struc = serterms[1]
    webpage = serterms[3]

    terms = [currency, flatfees_struc, partnership_struc, webpage]
    serterms = serialize_array(terms)
    Put(ctx,adr, serterms)

    msg = concat("Partnership updated:", " ")
    a = concat("Address : ", adr)
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


def set_flatfees(adr, flatfees_struc):
    msg = concat("Change flatfees structure for: ", adr)
    Notify(msg)

    termsba = Get(ctx,adr)
    if not termsba:
        Notify("Partnership for address is not yet created")
        return False
    serterms = deserialize_bytearray(termsba)
    currency = serterms[0]
    partnership_struc = serterms[2]
    webpage = serterms[3]

    terms = [currency, flatfees_struc, partnership_struc, webpage]
    serterms = serialize_array(terms)
    Put(ctx,adr, serterms)

    msg = concat("Partnership updated:", " ")
    a = concat("Address : ", adr)
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


def set_webpage(adr, webpage):
    msg = concat("Change webpage for: ", adr)
    Notify(msg)
    termsba = Get(ctx,adr)
    if not termsba:
        Notify("Partnership for address is not yet created")
        return False
    serterms = deserialize_bytearray(termsba)
    currency = serterms[0]
    flatfees_struc = serterms[1]
    partnership_struc = serterms[2]

    terms = [currency, flatfees_struc, partnership_struc, webpage]
    serterms = serialize_array(terms)
    Put(ctx, adr, serterms)

    msg = concat("Webpage updated:", " ")
    a = concat("Address : ", adr)
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


def serialize_array(items):

    # serialize the length of the list
    itemlength = serialize_var_length_item(items)

    output = itemlength

    # now go through and append all your stuff
    for item in items:
        # get the variable length of the item
        # to be serialized
        itemlen = serialize_var_length_item(item)

        # add that indicator
        output = concat(output, itemlen)

        # now add the item
        output = concat(output, item)

    # return the stuff
    return output


def serialize_var_length_item(item):

    # get the length of your stuff
    stuff_len = len(item)

    # now we need to know how many bytes the length of the array
    # will take to store

    # this is one byte
    if stuff_len <= 255:
        byte_len = b'\x01'
    # two byte
    elif stuff_len <= 65535:
        byte_len = b'\x02'
    # hopefully 4 byte
    else:
        byte_len = b'\x04'

    out = concat(byte_len, stuff_len)

    return out


def deserialize_bytearray(data):

    # ok this is weird.  if you remove this print statement, it stops working :/

    # get length of length
    collection_length_length = data[0:1]

    # get length of collection
    collection_len = data[1:collection_length_length + 1]

    # create a new collection
    new_collection = list(length=collection_len)

    # trim the length data
    offset = 1 + collection_length_length

    for i in range(0, collection_len):

        # get the data length length
        itemlen_len = data[offset:offset + 1]

        # get the length of the data
        item_len = data[offset + 1:offset + 1 + itemlen_len]

        # get the data
        item = data[offset + 1 + itemlen_len: offset + 1 + itemlen_len + item_len]

        # store it in collection
        new_collection[i] = item

        offset = offset + item_len + itemlen_len + 1

    return new_collection
