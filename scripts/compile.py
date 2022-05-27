from script_utils import create_compile_command, run_command

CONTRACTS_TO_COMPILE = [
    [
        "ZUSD",
        "ZUSD",
    ],
    ["ZUSD_Proxy",
     "ZUSD_Proxy"]
]

for contract in CONTRACTS_TO_COMPILE:
    cmd = create_compile_command(contract[0], contract[1])
    w = run_command(cmd)
