import json
import sys

TERMINATORS = "jmp", "br", "ret"

def form_blocks(instructions):
    curr_block = []
    for inst in instructions:
        # Checking if the instruction is a label (or) a normal instruction.
        if "op" in inst:
            # This is a normal instruction.
            curr_block.append(inst)

            # Checking if the instruction was a terminator.
            if inst["op"] in TERMINATORS:
                # This is a terminator instructions and we need to yeild the current block.
                yield curr_block
                # Start a new empty block.
                curr_block = []
        else:
            # This is a label.
            # We need to yeild the block.
            yield curr_block
            # Then start the new block with the label.
            curr_block = [inst]
    # Now if the program reached to this stage which means there is an imlicit return.
    yield curr_block

def createCFG(blocks):
    # We need to loop over the blocks.
    for block in blocks:
        last_instruction = block[-1]
        print(block)
        # Now here I want to implement the logic to create a CFG.




def processCFG():
    out  = {}
    prog = json.load(sys.stdin)
    blocks = []
    for func in prog["functions"]:
        for block in form_blocks(func["instr"]):
            print(block)
        blocks.append(form_blocks(func["instr"]))
    createCFG(blocks)



if __name__ == __main__:
    processCFG()