namespace IfAndElse
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Tere! Kui vana olete?");
            int vanus = int.Parse(Console.ReadLine());                       
 
            if (vanus < 18)
            {
               Console.ForegroundColor = ConsoleColor.Blue;
               Console.WriteLine("Olete alaealine!");
            }
            else if (vanus >= 18 && vanus <= 65)
            {
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine("Olete täisealine!");
            }
            else if (vanus > 65)
            {
                Console.ForegroundColor = ConsoleColor.Yellow;
                Console.WriteLine("Olete pensionäär.");
            }                          
        }
    }
}
