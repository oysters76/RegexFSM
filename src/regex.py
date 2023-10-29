'''
 Simple regex parser that converts simple regex 
 expressions to a finite state machine (fsm)

 e.g. 
 regrex expression: abc$ 
 
 then the fsm looks like follows, 
 a -> b -> c -> END

'''

class StateColumn:
    def __init__(self, size):
        self.column = [0 for i in range(size)] 
    
    def mark(self, index, state):
        self.column[index] = state
    
    def get(self,index):
        return self.column[index]
    
class FSM:
    def __init__(self,size):
        self.states = [] 
        self.size = size 
    
    def push_state(self):
        self.states.append(StateColumn(self.size))

    def get_current_state(self):
        return len(self.states) - 1
    
    def get_size(self):
        return len(self.states)

    def get_next_state(self):
        return len(self.states)
    
    def state(self,ind=-1):
        if (ind == -1):
            return self.states[self.get_current_state()]
        return self.states[ind]
    
    def dump(self):
        for i in range(self.size):
            print(str(i).zfill(3)," => ", end="")
            for state in self.states:
                print(state.get(i)," ",end="")
            print()

def to_fsm(expression):
    fsm = FSM(128) 
    fsm.push_state() # Terminal state
    for token in expression:
        fsm.push_state()
        if (token == "$"):
            fsm.state().mark(127, fsm.get_next_state())
            continue
        fsm.state().mark(ord(token), fsm.get_next_state())
    return fsm 

def run_fsm(fsm, text):
    current_state = 1
    for token in text:
        if current_state == 0 or current_state > fsm.get_size():
            break
        current_state = fsm.state(current_state).get(ord(token))
    
    if current_state == 0:
        return False 

    if current_state > fsm.get_size():
        return False 
    
    return current_state <= fsm.get_size()

fsm = to_fsm("abc$") 
fsm.dump()
print(run_fsm(fsm, "abc"))


        
        


