using System.ComponentModel.Design;

namespace RandomNumbers
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int number = new Random().Next(1,7);
            switch (number)
            {
                case int i when (i >= 1 && i <= 6):                 
                    Console.WriteLine("Veeretasid: " + number);
                    break;
                default:
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("Err");
                    break;
            }       
        }
    }
}
