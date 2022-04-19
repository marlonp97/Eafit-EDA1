// Punto 1

// Miguel Angel Sarmiento Aguiar
// Marlon Perez Rios

import java.util.*;

public static int polaca  (String string){
    String[] prefixStr = string.split(" "); 
    Stack<Integer> stack = new Stack<>();
    
    for(int i=0;i<prefixStr.length;i++){
        if(prefixStr[i].equals("+")){
            stack.push(stack.pop() + stack.pop());
        }
        else if(prefixStr[i].equals("*")){
            stack.push(stack.pop() * stack.pop());
        }
        else if(prefixStr[i].equals("-")){
            stack.push(stack.pop() - stack.pop());
        }
        else if(prefixStr[i].equals("/")){
            stack.push(stack.pop() / stack.pop());
        }
        else{
            stack.push(Integer.parseInt(prefixStr[i]));
        }
    }
    return stack.pop();
}
