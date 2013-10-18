public class Problem370{
  
  public static void main(String[] args){
    int n = 10000;
    
    long startTime = System.currentTimeMillis();
    System.out.println(doit(n));
    System.out.println("Time: " + (System.currentTimeMillis() - startTime) + " milliseconds");
    
    /*
    startTime = System.currentTimeMillis();
    System.out.println(bf(n));
    System.out.println("Time: " + (System.currentTimeMillis() - startTime) + " milliseconds");
    */
  }
  
  private static int doit(int limit){
    int count = 0;
    for(int c = 1; c <= limit / 2; c++){
      for(int b = 1; b <= c; b++){
        for(int a = 1; a <= b; a++){
          if (a + b + c <= limit && a + b > c && b*b == a*c){
            count++;
          }
        }
      }
    }
    return count;
  }
  
  private static int bf(int limit){
    int count = 0;
    for(int c = 1; c <= limit; c++){
      for(int b = 1; b <= limit; b++){
        for(int a = 1; a <= limit; a++){
          if (b*b == a*c && a + b + c <= limit && a + b > c && a <= b && b <= c){
            count++;
            // System.out.println(a + " " + b + " " + c);
          }
        }
      }
    }
    return count;
  }
  
}