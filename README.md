# IDAPython-Function-finder-by-xrefs
Find a function in IDA Pro by supplying addresses of functions that you know are called by the unknown function.

**Parameters in the code:**

- adrs: list of addresses that are called by the function you want to search.
- callsNum: minimum number of times the address (at the same index as adrs) is called.
- strict: If set to True the address must be called the number of times set in callNum and not greater.
