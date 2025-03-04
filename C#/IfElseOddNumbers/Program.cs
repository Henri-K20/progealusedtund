namespace IfElseOddNumbers
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int number = int.Parse(Console.ReadLine());

            if (number % 2 == 0 )
            {
                Console.WriteLine("Paaris");
            }
            else if (number % 2 != 0 )
            {
                Console.WriteLine("Paaritu");
            }
        }
    }
}
