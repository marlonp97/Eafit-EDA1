// Punto 2

// Miguel Angel Sarmiento Aguiar
// Marlon Perez Rios

import java.util.*;

public void neveras (Queue<String> nev, Stack<String> sol){
        
      while(!nev.isEmpty() && !sol.empty()){
          String nevera = nev.poll();
          String tienda = sol.pop();
          System.out.println("Entregar la nevera "+ nevera + " a la tienda " + tienda);
      }
}
