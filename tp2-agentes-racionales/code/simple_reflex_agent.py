import sys
import os
from typing import Optional
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_agent import BaseAgent
import random

def random_choice():
    x = random.randint(0, 3)
    return x


class simple_reflex_agent(BaseAgent):
    
    def __init__(self, server_url: str = "http://localhost:5000", 
                 enable_ui: bool = False,
                 record_game: bool = False, 
                 replay_file: Optional[str] = None,
                 cell_size: int = 60,
                 fps: int = 10,
                 auto_exit_on_finish: bool = True,
                 live_stats: bool = False):
        super().__init__(server_url, "Simple_Reflex_Agent", enable_ui, record_game, 
                        replay_file, cell_size, fps, auto_exit_on_finish, live_stats)
        
        # Estado interno para movimiento random
        self.movement_sequence = [self.up, self.right, self.down, self.left]
        self.current_move_index = random_choice()
    
    def get_strategy_description(self) -> str:
        return "Clean if dirty, move randomly (up, down, left, right)"
    
    def think(self) -> bool:
        
        if not self.is_connected():
            return False
        
        perception = self.get_perception()
        if not perception or perception.get('is_finished', True):
            return False
        
        # REGLA 1: Si hay suciedad, limpiar
        if perception.get('is_dirty', False):
            return self.suck()
        
        # REGLA 2: Moverse en patrón Random (arriba, derecha, abajo, izquierda)
        move_function = self.movement_sequence[self.current_move_index]
        success = move_function()
        
        # Avanzar al siguiente movimiento en la secuencia
        self.current_move_index = random_choice()
        
        return success

def run_example_agent_simulation(size_x: int = 8, size_y: int = 8, 
                                dirt_rate: float = 0.3, 
                                server_url: str = "http://localhost:5000",
                                verbose: bool = True) -> int:
    """
    Función de conveniencia para ejecutar una simulación con ExampleAgent.
    """
    agent = simple_reflex_agent(server_url)
    
    try:
        if not agent.connect_to_environment(size_x, size_y, dirt_rate):
            return 0
        
        performance = agent.run_simulation(verbose)
        return performance
    
    finally:
        agent.disconnect()

if __name__ == "__main__":
    print("Example Agent - Random Movement Pattern")
    print("Make sure the environment server is running on localhost:5000")
    print("Strategy: Clean if dirty, move randomly (up, down, left, right)")
    print()
    
    performance = run_example_agent_simulation(verbose=True)
    print(f"\nFinal performance: {performance}")