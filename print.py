"""
Test & Build: neo> build ../neoPartnershipContract/print.py test 07 05 True False main
Import:       neo> import contract ../neoPartnershipContract/print.avm 07 05 True False
Invoke:       neo> testinvoke <hash> main
"""
from boa.interop.Neo.Runtime import Log, Notify
from boa.builtins import list

def Main():
    print("log via print (1)")
    Log("normal log (2)")
    Notify("notify (3)")

    # Sending multiple arguments as notify payload:
    msg = ["a", 1, 2, b"3"]
    Notify(msg)

    return ["A","B","C"]

