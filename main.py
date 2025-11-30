from fastapi import FastAPI 

app = FastAPI() 

@app.get("/reward")
def reward(block_index: int): 
    base_reward = 50 
    halving_interval = 2 
    halvings = block_index // halving_interval
    return {"reward": base_reward / (2 ** halvings)}