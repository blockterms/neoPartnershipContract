"""
blockterms simple partnership contract
======================================
Author: Anil Kumar
Email: yak@fastmail.com
Date: Dec 22 2018
"""

from boa.blockchain.vm.Neo.Runtime import GetTrigger, CheckWitness, Notify
from boa.blockchain.vm.Neo.TriggerType import Application, Verification
from blockterms.partnership import Partnership
from boa.blockchain.vm.Neo.Runtime import Log, Notify

#
# This is the script hash of the address for the owner of the token
# This can be found in ``neo-python`` with the walet open, use ``wallet`` command
# Use the correct one for private or test or main network
#
owner = b'#\xba\'\x03\xc52c\xe8\xd6\xe5"\xdc2 39\xdc\xd8\xee\xe9'
arg_error = 'Incorrect Arg Length'


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
    if trigger == Verification:

        is_owner = CheckWitness(owner)

        if is_owner:
            return True
        else:
            return False

    elif trigger == Application:

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
    is_owner = CheckWitness(owner)

    if is_owner:
        if nargs == 5:
            address = args[0]
            currency = args[1]
            flatfees_struc = args[2]
            partnership_struc = args[3]
            webpage = args[4]
            pship = Partnership()
            pship.create_partnership(address,currency,flatfees_struc,partnership_struc,webpage)
            return False
        Notify(arg_error)
        return False
    else:
        Notify("Unauthorized to create Partnership")
        return False


def do_transfer(args):
    is_owner = CheckWitness(owner)

    if is_owner:
        if len(args) == 2:
            from_address = args[0]
            to_address = args[1]
            pship = Partnership()
            pship.transfer(from_address,to_address)
            return True
        Notify(arg_error)
        return False
    else:
        Notify("Unauthorized to transfer Partnership")
        return False


def do_info(args):
    nargs = len(args)
    if nargs == 1:
        address = args[0]
        pship = Partnership()
        pship.print_info(address)
        return True
    Notify(arg_error)
    return False


def do_delete_partnership(args):
    is_owner = CheckWitness(owner)

    if is_owner:
        nargs = len(args)
        if nargs == 1:
            address = args[0]
            pship = Partnership()
            pship.delete(address)
            return True
        Notify(arg_error)
        return False
    else:
        Notify("Unauthorized to delete Partnership")
        return False


def do_set_percentage_partnership(args):
    is_owner = CheckWitness(owner)
    if is_owner:
        nargs = len(args)
        if nargs == 2:
            address = args[0]
            partnership_struc = args[1]
            pship = Partnership()
            pship.set_partnership(address,partnership_struc)
            return True
        Notify(arg_error)
        return False
    else:
        Notify("Unauthorized to edit Partnership")
        return False


def do_set_flatfee_partnership(args):
    is_owner = CheckWitness(owner)
    if is_owner:
        nargs = len(args)
        if nargs == 2:
            address = args[0]
            flatfee_struc = args[1]
            pship = Partnership()
            pship.set_flatfees(address, flatfee_struc)
            return True
        Notify(arg_error)
        return False
    else:
        Notify("Unauthorized to edit Partnership")
        return False

def do_set_webpage(args):
    is_owner = CheckWitness(owner)
    if is_owner:
        nargs = len(args)
        if nargs == 2:
            address = args[0]
            webpage = args[1]
            pship = Partnership()
            pship.set_webpage(address, webpage)
            return True
        Notify(arg_error)
        return False
    else:
        Notify("Unauthorized to edit Partnership")
        return False
